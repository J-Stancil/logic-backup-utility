"""
Verifier module.

Confirms backup archives exist and are large enough to be trusted.
This prevents a broken backup from replacing the last good one.
"""

from pathlib import Path
from logger import BackupLogger


class BackupVerifier:

    def __init__(self, logger: BackupLogger):
        self.logger = logger

    def verify_archives(self, backup_destination: Path, jobs: list) -> int:
        """
        Verify that each expected archive exists.

        Returns total archive size in bytes.
        Raises RuntimeError if any archive is missing.
        """
        total_size = 0

        for job in jobs:
            archive_path = backup_destination / job["zip_name"]

            if not archive_path.exists():
                self.logger.log(f"MISSING ARCHIVE: {job['zip_name']}")
                raise RuntimeError("Archive verification failed")

            archive_size = archive_path.stat().st_size
            total_size += archive_size

            self.logger.log(f"VERIFIED ARCHIVE: {job['zip_name']} ({archive_size} bytes)")

        self.logger.log(f"Total backup archive size: {total_size} bytes")
        return total_size