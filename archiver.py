"""
Archiver module.

Creates one zip archive per staged backup category.
This preserves the user's preferred manual-restore workflow.
"""

import shutil
from pathlib import Path
from logger import BackupLogger


class BackupArchiver:

    def __init__(self, logger: BackupLogger):
        self.logger = logger

    def create_archives(self, staging_run: Path, backup_destination: Path, jobs: list) -> None:
        """
        Create one zip file per staged category.

        Each staged folder is compressed individually so restore remains simple
        and the resulting backup set mirrors the user's previous working model.
        """
        for job in jobs:
            staged_folder = staging_run / job["name"]
            zip_stem = job["zip_name"].replace(".zip", "")
            zip_base_path = backup_destination / zip_stem

            self.logger.log(f"Archiving: {job['name']}")

            shutil.make_archive(
                base_name=str(zip_base_path),
                format="zip",
                root_dir=str(staged_folder.parent),
                base_dir=staged_folder.name,
            )

            self.logger.log(f"Created archive: {job['zip_name']}")