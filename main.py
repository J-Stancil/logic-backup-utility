"""
Logic Backup Utility Main Orchestrator
"""

from pathlib import Path
from config import *
from logger import BackupLogger
from scanner import BackupScanner
from stager import BackupStager
from archiver import BackupArchiver
from manifest import BackupManifest
from verifier import BackupVerifier
from rotator import BackupRotator
from notifier import BackupNotifier


def run_backup():

    log_file = STAGING_DIR / "backup_log.txt"
    logger = BackupLogger(log_file)

    notifier = BackupNotifier(logger, "YOUR_EMAIL_HERE")

    try:
        logger.log("Backup started")

        scanner = BackupScanner(BACKUP_SOURCES, logger)
        jobs = scanner.validate_sources()

        stager = BackupStager(STAGING_DIR, logger)
        staging_run = stager.prepare_staging()
        stager.stage_sources(jobs, staging_run)

        manifest = BackupManifest(logger)
        manifest.generate_manifest(staging_run)

        backup_destination = ICLOUD_BACKUP_ROOT / staging_run.name
        backup_destination.mkdir(parents=True)

        archiver = BackupArchiver(logger)
        archiver.create_archives(staging_run, backup_destination, jobs)

        verifier = BackupVerifier(logger)
        verifier.verify_archives(backup_destination, jobs)

        rotator = BackupRotator(logger)
        rotator.rotate_old_backups(ICLOUD_BACKUP_ROOT, MAX_BACKUPS)

        notifier.send_success()

        logger.log("Backup completed successfully")

    except Exception as e:
        logger.log(f"Backup failed: {e}")
        notifier.send_failure(log_file)


if __name__ == "__main__":
    run_backup()