#!/usr/bin/env python
"""
Python CLI tool that allows checking Ricoh printers supply/toner status.

Usage: python main.py <IP_ADDRESS>
"""
import ipaddress
import sys

import typer
from easysnmp import Session
from easysnmp.exceptions import EasySNMPError, EasySNMPTimeoutError


# OIDs
model_name_code         = '.1.3.6.1.2.1.43.5.1.1.16.1'
serial_num_code         = '.1.3.6.1.2.1.43.5.1.1.17.1'
supply_names_snmp_code  = '.1.3.6.1.2.1.43.12.1.1.4.1'
supply_levels_snmp_code = '.1.3.6.1.2.1.43.11.1.1.9.1'


def snmp_request(ip):
    try:
        # Create an SNMP session to be used for all our requests
        session = Session(hostname=ip, community='public', version=2, timeout=2, retries=1, abort_on_nonexistent=True)

        model_name = session.get(model_name_code).value
        serial_num = session.get(serial_num_code).value

        # Perform an SNMP walk
        supply_names_snmp = session.walk(supply_names_snmp_code)
        supply_levels_snmp = session.walk(supply_levels_snmp_code)

        supply_names  = []
        supply_levels = []

        # Skip waste toner cartridge (index start from 0)
        supply_names.extend(item.value for i, item in enumerate(supply_names_snmp) if i != 1)
        supply_levels.extend(item.value for i, item in enumerate(supply_levels_snmp) if i != 1)

        # {'black': '80', 'cyan': '90', 'magenta': '90', 'yellow': '80'}
        supply_status = dict(zip(supply_names, supply_levels))

        result = {'ip': ip, 'model': model_name, 'serial': serial_num, 'supplyStatus': supply_status}
    # https://easysnmp.readthedocs.io/en/latest/exceptions.html
    except EasySNMPTimeoutError as e:
        exit_with_msg(f'Request timed out while connecting to remote host {ip}')
    except EasySNMPError as e:
        exit_with_msg(f'Something went wrong: {e}')
    else:
        return result


def exit_with_msg(msg):
    print(f'[ERROR] {msg}')
    sys.exit(0)


def progress_bar(count, text=''):
    bar_len    = 40
    total      = 100
    empty_fill = '-'  # ∙
    fill       = '='  # ▣ ◉

    if isinstance(count, str):
        count = 0
        percents = 'N/A'
    else:
        percents = f'{round(100 * int(count) / float(total))}%'

    filled_len = int(round(bar_len * count / float(total)))
    bar        = fill * filled_len + empty_fill * (bar_len - filled_len)

    return f'[{bar}] {percents} {text}\r'


def validate_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"The IP address '{ip}' is not valid")
        sys.exit(0)


def main(ip):

    validate_ip_address(ip)

    result = snmp_request(ip)

    print(f"ip: {result['ip']} - model: {result['model']} - serial: {result['serial']}\n")

    for key, value in result['supplyStatus'].items():
        print(progress_bar(value, key))


if __name__ == '__main__':
    typer.run(main)
