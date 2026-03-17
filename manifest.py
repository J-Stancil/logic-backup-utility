"""
Manifest module.

Creates a readable inventory of backup contents.
Also prepares baseline data for future verification logic.
"""

from pathlib import Path
from logger import BackupLogger


class BackupManifest:

    def __init__(self, logger: BackupLogger):
        self.logger = logger

    def generate_manifest(self, staging_run: Path) -> Path:
        """
        Generates a human-readable inventory file.
        """
        manifest_file = staging_run / "backup_manifest.txt"

        with manifest_file.open("w", encoding="utf-8") as f:
            for item in staging_run.iterdir():
                if item.is_dir():
                    f.write(f"{item.name}\n")

        self.logger.log("Manifest generated")

        return manifest_file