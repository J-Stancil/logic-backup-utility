<p align="center">
  <img src="logo.png" width="160">
</p>

# Logic Backup Utility

Automated disaster recovery system for Logic Pro plugin and configuration environments.

Automated macOS backup utility for Logic Pro workflow recovery.

## Overview

This project backs up critical Logic-adjacent data and plugin files into dated archive sets stored in iCloud Drive.

It was built to solve a real workflow problem:

I do not use full-system backup tools like Time Machine consistently, but I still need a practical rescue path if my internal drive fails.

Instead of backing up entire projects, this utility focuses on the parts of my environment that would take the most time to rebuild manually.

## Core Purpose

- Back up Logic-related configuration data
- Back up installed plugin formats used in my workflow
- Create individually zipped backup categories
- Store backup sets in iCloud Drive
- Keep backup structure simple enough for manual restore

## Technical Design

This utility follows a modular architecture:

- `scanner.py` → validates source directories
- `stager.py` → prepares staging backup structure
- `archiver.py` → builds ZIP archives safely
- `verifier.py` → confirms archive integrity
- `rotator.py` → enforces backup retention policy
- `notifier.py` → handles success / failure email logic
- `logger.py` → writes timestamped execution logs
- `main.py` → orchestrates backup workflow

## Reliability Features

- Pre-backup validation of required paths
- Timestamped staging runs
- Archive verification before cleanup
- Automated retention rotation
- Failure-safe logging
- Designed for unattended execution (cron / launchd)

## Intended Use Case

Professional audio environments where:

- System rebuild time must be minimized
- Plugin environments must be reproducible
- Backup strategy must be deterministic
- Full disk imaging is not always practical


## How to Run

1. Clone repository

```bash
git clone https://github.com/J-Stancil/logic-backup-utility.git
cd logic-backup-utility

## Current Backup Scope

This utility currently backs up:

- Audio Unit plug-ins (`Components`)
- VST3 plug-ins
- Waves plugin shell support (`WPAPI`)
- Logic Channel Strip Settings
- Logic Plug-In Settings / Presets
- Logic Sampler Instruments
- Logic Patches
- Logic Project Templates

## Notes

- Backup sets are stored as individually zipped categories
- Restores are currently manual by design
- Temporary staging data is removed after a successful run
- Only the most recent verified backup is retained

## Design Philosophy

This project was intentionally built as a focused operational tool rather than a generalized backup system.

Key principles:

- Deterministic backups over full-system imaging
- Simple restore path over automation complexity
- Modular architecture to support future expansion
- Real-world workflow driven design
- Reliability over feature density

## Future Improvements

- Launchd automation profile
- Backup integrity baseline learning
- Selective restore tooling
- UI wrapper for non-technical users
- Multi-destination backup support
- Performance optimization for large plugin libraries

## Author

Jason Stancil  
Audio Engineer / IT Professional / Systems Automation Learner