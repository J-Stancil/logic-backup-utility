"""
Notifier module.

Handles success and failure email notifications via macOS Mail.
"""

import subprocess
from pathlib import Path
from logger import BackupLogger


class BackupNotifier:
    def __init__(self, logger: BackupLogger, email_address: str):
        self.logger = logger
        self.email_address = email_address

    def send_email(self, subject: str, body: str, attachment: Path | None = None) -> None:
        attachment_script = ""

        if attachment and attachment.exists():
            attachment_script = f'''
                tell newMessage
                    make new attachment with properties {{file name:POSIX file "{attachment}"}} at after the last paragraph
                end tell
            '''

        applescript = f'''
        tell application "Mail"
            activate
            set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}", visible:false}}
            tell newMessage
                make new to recipient at end of to recipients with properties {{address:"{self.email_address}"}}
            end tell
            {attachment_script}
            send newMessage
            delay 3
            quit
        end tell
        '''

        subprocess.run(["osascript", "-e", applescript], check=False)

    def send_success(self) -> None:
        self.logger.log("Sending success email")
        self.send_email(
            subject="Logic Backup Success",
            body="Backup completed and verified successfully."
        )

    def send_failure(self, log_file: Path) -> None:
        self.logger.log("Sending failure email")
        self.send_email(
            subject="Logic Backup Failure",
            body="Backup failed. See attached log.",
            attachment=log_file
        )