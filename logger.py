"""
Logging utilities for Logic Backup Utility.

This module creates a readable plain-text log so each run can be reviewed later.
The log is also attached to failure emails.
"""

from pathlib import Path
from datetime import datetime


class BackupLogger:
    """
    Simple backup logger that writes timestamped lines to a text file.
    """

    def __init__(self, log_file: Path) -> None:
        self.log_file = log_file

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {message}"

        print(line)

        with self.log_file.open("a", encoding="utf-8") as file:
            file.write(line + "\n")