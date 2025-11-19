import re
import argparse
from collections import Counter

def load_blacklist(blacklist_file):
    """Load a list of suspicious IPs from a file."""
    try:
        with open(blacklist_file, 'r') as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        print(f"[!] Blacklist file {blacklist_file} not found. Continuing without it.")
        return set()

def analyze_logs(log_file, blacklist_ips):
    """Analyze the log file for security events."""
    failed_login_pattern = r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)'
    failed_logins = []
    blacklist_hits = []

    try:
        with open(log_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                # Check for failed login patterns
                failed_match = re.search(failed_login_pattern, line)
                if failed_match:
                    ip = failed_match.group(1)
                    failed_logins.append(ip)
                    print(f"[!] Failed login detected from IP: {ip} (Line {line_num})")

                # Check if any IP in the line is on the blacklist
                for ip in blacklist_ips:
                    if ip in line:
                        blacklist_hits.append((ip, line_num))
                        print(f"[!] Blacklisted IP '{ip}' found on line {line_num}")

    except FileNotFoundError:
        print(f"[!] Error: Log file {log_file} not found.")
        return

    # Generate a summary report
    print("\n" + "="*50)
    print("SCAN SUMMARY REPORT")
    print("="*50)
    print(f"Total failed login attempts: {len(failed_logins)}")
    if failed_logins:
        top_offender = Counter(failed_logins).most_common(1)[0]
        print(f"Most frequent offending IP: {top_offender[0]} ({top_offender[1]} attempts)")
    print(f"Total blacklist IP matches: {len(blacklist_hits)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Log Analyzer for Blue Team Security")
    parser.add_argument("logfile", help="Path to the log file to analyze")
    parser.add_argument("--blacklist", help="Path to a file containing a list of suspicious IPs (one per line)", default="blacklist.txt")

    args = parser.parse_args()

    blacklist_ips = load_blacklist(args.blacklist)
    analyze_logs(args.logfile, blacklist_ips)
