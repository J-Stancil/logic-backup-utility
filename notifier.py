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
        self.logo_path = Path(__file__).resolve().parent / "LOGO.png"

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

        body = """Logic Backup System

Status: SUCCESS

Backup completed and verified successfully.
The latest backup set has been archived and staged cleanup has completed.
"""

        self.send_email(
            subject="Logic Backup Success",
            body=body
        )

    def send_failure(self, log_file: Path) -> None:
        self.logger.log("Sending failure email")

        body = """Logic Backup System

Status: FAILURE

The backup process did not complete successfully.
See attached log for details.
"""

        self.send_email(
            subject="Logic Backup Failure",
            body=body,
            attachment=log_file
        )

        