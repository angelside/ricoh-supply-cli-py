# Ricoh Supply CLI

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciICB2aWV3Qm94PSIwIDAgNDggNDgiIHdpZHRoPSI0OHB4IiBoZWlnaHQ9IjQ4cHgiPjxwYXRoIGZpbGw9IiM0Y2FmNTAiIGQ9Ik0yNCw1QzEzLjUsNSw1LDEzLjYsNSwyNC4xYzAsOC4yLDUuMSwxNS4xLDEyLjMsMTcuOWw0LjItMTEuNUMxOC44LDI5LjUsMTcsMjcsMTcsMjQgYzAtMy45LDMuMS03LDctN3M3LDMuMSw3LDdjMCwzLTEuOCw1LjUtNC41LDYuNUwzMC43LDQyQzM3LjksMzkuMiw0MywzMi4zLDQzLDI0LjFDNDMsMTMuNiwzNC41LDUsMjQsNXoiLz48cGF0aCBmaWxsPSIjMmU3ZDMyIiBkPSJNMTcuOSw0My4zbC0wLjktMC40QzkuMiw0MCw0LDMyLjQsNCwyNC4xQzQsMTMsMTMsNCwyNCw0YzExLDAsMjAsOSwyMCwyMC4xIGMwLDguMy01LjIsMTUuOS0xMi45LDE4LjhsLTAuOSwwLjRsLTQuOC0xMy4zbDAuOS0wLjRjMi4zLTAuOSwzLjgtMy4xLDMuOC01LjZjMC0zLjMtMi43LTYtNi02cy02LDIuNy02LDZjMCwyLjUsMS41LDQuNywzLjgsNS42IGwwLjksMC40TDE3LjksNDMuM3ogTTI0LDZDMTQuMSw2LDYsMTQuMSw2LDI0LjFjMCw3LjEsNC4zLDEzLjcsMTAuNywxNi41bDMuNS05LjZDMTcuNiwyOS43LDE2LDI3LDE2LDI0YzAtNC40LDMuNi04LDgtOCBzOCwzLjYsOCw4YzAsMy0xLjYsNS43LTQuMiw3bDMuNSw5LjZDMzcuNywzNy44LDQyLDMxLjMsNDIsMjQuMUM0MiwxNC4xLDMzLjksNiwyNCw2eiIvPjwvc3ZnPg==)](./LICENSE)
[![GitHub-Sponsors](https://img.shields.io/badge/Sponsor-EA4AAA.svg?style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/angelside)

> Ricoh Supply CLI is a _"blazingly fast 🤣"_ Python CLI tool that allows checking Ricoh printers supply/toner status with SNMP protocol.

### Windows is not supported

> __Warning__ - Windows installation is failing

I tested in Windows 11 with Python 3.11.1, and it's failing. I think easysnmp doesn't have proper windows support.

```✖ Install easysnmp 0.2.6 failed```

## 📦 Installation

Clonning the repo

```bash
git clone https://github.com/angelside/ricoh-supply-cli-py.git ricoh-supply-cli-py
```

```
cd ricoh-supply-cli-py
```

Use the package manager [pdm](https://pdm.fming.dev/) to install. Run the below command inside the project directory.

```bash
pdm install
```

## 🔨 Usage

CLI app has only one parameter and that is the IP address of the printer.

```bash
python main.py 172.10.0.2
```

or

```bash
chmod +x main.py
./main.py 172.10.0.2
```

### 📋 Sample results

cmyk

```bash
> ./main.py 172.10.0.2
ip: 172.10.0.2 - model: MP C307 - serial: 11111111111

[====================================----] 90.0%  black
[============----------------------------] 30.0%  cyan
[============----------------------------] 30.0%  magenta
[========--------------------------------] 20.0%  yellow
```

only black

```bash
./main.py 172.10.0.3
ip: 172.10.0.3 - model: P 502 - serial: 22222222222

[============================------------] 70.0%  black
```

## 💥 Features

- Retrieves; model, serial, toner level status
- Progress bar
- Ip address validation
- SNMP exceptions

## 🎯 Tested Ricoh printer models

- IM C300 (cmyk)
- IM C3500 (cmyk)
- MP C307 (cmyk)
- P 502 (black)

## 🤝 Contributing

Before contributing issues or pull requests, be sure to review the [Contributing Guidelines](./.github/CONTRIBUTING.md) first.

## 💬 Questions?

Feel free to [open an issue](http://github.com/angelside/ricoh-supply-cli-py/issues/new).

## 🤩 Support

💙 If you like this project, give it a ⭐ and share it with friends!

[![GitHub-Sponsors](https://img.shields.io/badge/GitHub%20Sponsor-EA4AAA.svg?style=for-the-badge&logo=GitHub-Sponsors&logoColor=white)](https://github.com/sponsors/angelside)

## 🏛️ License

This project is open-sourced software licensed under the [MIT license](./LICENSE).