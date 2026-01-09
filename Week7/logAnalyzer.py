import re
import logging
from collections import Counter

# I used Gemini to genmerate comments for this code.

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogEntry:
    # Represents a single log entry and provides methods for parsing it.
    def __init__(self, line):
        self.line = line
        self.timestamp = None
        self.level = None
        self.message = None
        self.ip = None
        self.security_issue = None
        self.parse()

    def parse(self):
        # Parses the log line to extract timestamp, level, and message of apache style logs.
        match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (INFO|WARNING|ERROR) - (.*)', self.line)
        if match:
            self.timestamp, self.level, self.message = match.groups()
            if self.level == 'WARNING':
                self.parse_security_issue()
        else:
            logging.warning(f"Could not parse log line: {self.line}")

    def parse_security_issue(self):
        # Parses warning messages to identify specific types of security issues.
        patterns = {
            'Forbidden Access': r'Forbidden access attempt: ([\d.]+) -> .*',
            'SQL Injection': r'Potential SQL injection: ([\d.]+) -> . *',
            'Brute Force': r'Brute force attempt from ([\d.]+) - . *'
        }
        for issue, pattern in patterns.items():
            match = re.match(pattern, self.message)
            if match:
                self.ip = match.group(1)
                self.security_issue = issue
                break

class LogAnalyzer:
    # Analyzes a log file by reading and parsing its entries.
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_entries = []
        logging.info(f"Starting analysis of {self.log_file}")
        self.read_logs()
        logging.info(f"Finished analysis. Found {len(self.log_entries)} entries.")

    def read_logs(self):
        # Reads the log file and creates LogEntry objects for each line.
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    self.log_entries.append(LogEntry(line.strip()))
        except FileNotFoundError:
            logging.error(f"Log file not found: {self.log_file}")

    def count_by_level(self):
        # Counts the number of log entries for each log level.
        return Counter(entry.level for entry in self.log_entries if entry.level)

    def get_security_issues(self):
        # Gets a list of all identified security issues.
        issues = []
        for entry in self.log_entries:
            if entry.security_issue:
                issues.append({
                    'timestamp': entry.timestamp,
                    'issue': entry.security_issue,
                    'ip': entry.ip,
                    'message': entry.message
                })
        return issues

    def get_errors(self):
        # Returns all error messages.
        return [entry.message for entry in self.log_entries if entry.level == 'ERROR']

    def generate_report(self, report_file='/Users/1durch0/Studium/HTW Cyber Security & Business/1. Semester/Programming/Programming-Class/Week7/report.md'):
        # Generates a detailed report of the log analysis.
        logging.info(f"Generating report: {report_file}")
        with open(report_file, 'w') as f:
            f.write("# Log Analysis Report\n\n")

            f.write("## Summary\n")
            log_counts = self.count_by_level()
            f.write(f"- **Total Log Entries:** {len(self.log_entries)}\n")
            for level, count in log_counts.items():
                f.write(f"- **{level} Entries:** {count}\n")
            
            f.write("\n## Security Issues\n")
            security_issues = self.get_security_issues()
            if security_issues:
                issue_counts = Counter(issue['issue'] for issue in security_issues)
                for issue, count in issue_counts.items():
                    f.write(f"- **{issue}:** {count} occurrences\n")

                f.write("\n### Details of Security Issues\n")
                for issue in security_issues:
                    f.write(f"- **Timestamp:** {issue['timestamp']}\n")
                    f.write(f"  - **Type:** {issue['issue']}\n")
                    f.write(f"  - **IP Address:** {issue['ip']}\n")
                    f.write(f"  - **Log Message:** {issue['message']}\n\n")
            else:
                f.write("No security issues identified.\n")

            f.write("\n## Errors\n")
            errors = self.get_errors()
            if errors:
                for error in errors:
                    f.write(f"- {error}\n")
            else:
                f.write("No errors found in logs.\n")
        logging.info(f"Report generated successfully: {report_file}")

if __name__ == '__main__':
    analyzer = LogAnalyzer('/Users/1durch0/Studium/HTW Cyber Security & Business/1. Semester/Programming/Programming-Class/Week7/logs.txt')
    analyzer.generate_report()