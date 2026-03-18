"""
Staging module.

Copies validated backup sources into a visible Desktop staging area
before compression. This ensures transparency and recoverability.
"""

import shutil
from pathlib import Path
from datetime import datetime
from logger import BackupLogger


class BackupStager:

    def __init__(self, staging_root: Path, logger: BackupLogger):
        self.staging_root = staging_root
        self.logger = logger

    def prepare_staging(self) -> Path:
        """
        Creates a new dated staging directory.

        If staging exists, it is fully cleared first.
        """
        if self.staging_root.exists():
            self.logger.log("Clearing previous staging directory")
            shutil.rmtree(self.staging_root)

        self.staging_root.mkdir(parents=True)

        date_folder = datetime.now().strftime("%m.%d.%Y_%H-%M-%S")
        staging_run = self.staging_root / date_folder
        staging_run.mkdir()

        self.logger.log(f"Created staging run folder: {staging_run}")

        return staging_run

    def stage_sources(self, jobs: list, staging_run: Path):
        """
        Copies each validated source into staging.
        """
        for job in jobs:
            source_path = job["source"]
            target_path = staging_run / job["name"]

            self.logger.log(f"Staging: {job['name']}")

            shutil.copytree(source_path, target_path)

        self.logger.log("All sources staged successfully")