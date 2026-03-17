"""
Scanner module.

Validates backup sources before any data movement occurs.
This prevents partial or corrupt backups.
"""

from pathlib import Path
from typing import List, Dict
from logger import BackupLogger


class BackupScanner:

    def __init__(self, sources: List[Dict], logger: BackupLogger):
        self.sources = sources
        self.logger = logger

    def validate_sources(self) -> List[Dict]:
        """
        Validate backup source paths.

        Returns list of valid backup jobs.
        Aborts if required path missing.
        """
        valid_jobs = []

        for source in self.sources:
            path: Path = source["source"]

            if path.exists():
                self.logger.log(f"VALIDATED: {source['name']}")
                valid_jobs.append(source)

            else:
                if source["required"]:
                    self.logger.log(f"CRITICAL MISSING: {source['name']}")
                    raise RuntimeError("Required backup path missing")

                else:
                    self.logger.log(f"OPTIONAL MISSING: {source['name']}")

        return valid_jobs