# Blue Team Log Analyzer 🔍

A lightweight Python-based log analysis tool for Blue Team operations, designed to detect suspicious activities and security events in system logs.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)

## Features ✨

- **Failed Login Detection**: Identifies and reports failed authentication attempts
- **IP Blacklist Monitoring**: Cross-references log entries against known malicious IPs
- **Security Event Summary**: Generates comprehensive scan reports
- **Customizable Blacklists**: Easy integration with external IP threat intelligence
- **Real-time Alerts**: Immediate notification of suspicious activities during analysis

## Installation 🚀

### Prerequisites
- Python 3.6 or higher
- Read access to log files

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/Miasma01-d/blue-team-tools.git
cd blue-team-tools/log-analyzer

# No additional dependencies required - uses Python standard library!
