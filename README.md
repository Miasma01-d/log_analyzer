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
```
# No additional dependencies required - uses Python standard library!
Usage 📖
🎯 Important: You Need to Provide a Log File Path
The tool requires a path to a log file as input. Here are your options:

Option 1: Use Included Sample Logs
bash
# Use the provided sample log file
python3 log_analyzer.py sample_logs/auth_sample.log

# Or use the simple test log
python3 log_analyzer.py sample_logs/test_log.log
Option 2: Use Your Own Log File
bash
# Provide path to your own log file
```python3 log_analyzer.py /path/to/your/logfile.log```

# Examples for common log locations (Linux):
```python3 log_analyzer.py /var/log/auth.log
python3 log_analyzer.py /var/log/syslog
python3 log_analyzer.py /var/log/secure
```
Option 3: Create a Quick Test File
bash
```# Create a simple test log
echo "Failed password for root from 192.168.1.100" > my_test.log
echo "Successful login for user admin" >> my_test.log
echo "Failed password for user test from 103.107.198.125" >> my_test.log
```
# Analyze your test file
```python3 log_analyzer.py my_test.log```
With Custom Blacklist
bash
```# Use with the included blacklist
python3 log_analyzer.py sample_logs/auth_sample.log --blacklist blacklist.txt
```
# Or with your own blacklist file
```python3 log_analyzer.py /path/to/your/logfile.log --blacklist my_ips.txt```
Project Structure 🗂️
text
log_analyzer/
├── log_analyzer.py          # Main analysis script
├── README.md               # This file
├── LICENSE                 # MIT License
├── blacklist.txt           # Example IP blacklist
└── sample_logs/            # Sample log files for testing
    ├── auth_sample.log     # Sample authentication logs
    └── test_log.log        # Simple test log file 
Example Output 📊
```text
[!] Failed login detected from IP: 192.168.1.100 (Line 1)
[!] Failed login detected from IP: 103.107.198.125 (Line 3)
[!] Blacklisted IP '103.107.198.125' found on line 3

==================================================
SCAN SUMMARY REPORT
==================================================
Total failed login attempts: 2
Most frequent offending IP: 192.168.1.100 (1 attempts)
Total blacklist IP matches: 1
```
Configuration ⚙️
Blacklist Format
The blacklist.txt file should contain one IP address per line:

```text
103.107.198.125
185.220.101.204
45.95.147.229
```
Supported Log Formats
Linux auth.log (SSH failures)

Apache/nginx access logs

Custom application logs (with pattern modification)

Troubleshooting 🔧
Error: "the following arguments are required: logfile"

Solution: You forgot to specify a log file path. Use: python3 log_analyzer.py /path/to/logfile.log

Error: "Log file not found"

Solution: Check that the file path is correct and the file exists

Contributing 🤝
Contributions are welcome! Please feel free to submit pull requests or open issues for suggestions.
