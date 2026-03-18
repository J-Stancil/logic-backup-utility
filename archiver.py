"""
Archiver module.

Creates one zip archive per staged backup category.
This preserves the user's preferred manual-restore workflow.
"""

import zipfile
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
            archive_path = backup_destination / job["zip_name"]

            self.logger.log(f"Archiving: {job['name']}")

            with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                for file_path in staged_folder.rglob("*"):
                    if file_path.is_file():
                        relative_path = file_path.relative_to(staged_folder.parent)

                        # Force safe ZIP timestamp minimum (1980-01-01)
                        zip_info = zipfile.ZipInfo(str(relative_path))
                        zip_info.date_time = (1980, 1, 1, 0, 0, 0)

                        with file_path.open("rb") as f:
                            zf.writestr(zip_info, f.read(), compress_type=zipfile.ZIP_DEFLATED)

            self.logger.log(f"Created archive: {job['zip_name']}")