"""
Temporary notifier module.

Email sending is disabled during core engine debugging.
"""

from pathlib import Path
from logger import BackupLogger


class BackupNotifier:

    def __init__(self, logger: BackupLogger, email_address: str):
        self.logger = logger
        self.email_address = email_address

    def send_success(self):
        self.logger.log("SUCCESS EMAIL DISABLED DURING DEBUGGING")

    def send_failure(self, log_file: Path):
        self.logger.log(f"FAILURE EMAIL DISABLED DURING DEBUGGING: {log_file}")