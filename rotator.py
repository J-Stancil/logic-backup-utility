"""
Rotation module.

Deletes the previous verified backup only after a new backup succeeds.
"""

import shutil
from pathlib import Path
from logger import BackupLogger


class BackupRotator:

    def __init__(self, logger: BackupLogger):
        self.logger = logger

    def rotate_old_backups(self, backup_root: Path, keep_count: int) -> None:
        """
        Keep only the newest backup folders based on folder name sorting.
        """
        backup_folders = [item for item in backup_root.iterdir() if item.is_dir()]
        backup_folders.sort(reverse=True)

        old_backups = backup_folders[keep_count:]

        for old_backup in old_backups:
            self.logger.log(f"Deleting old backup: {old_backup}")
            shutil.rmtree(old_backup)