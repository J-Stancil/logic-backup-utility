"""
Configuration for Logic Backup Utility.

Defines:
- backup source locations
- staging directory
- iCloud backup destination
- retention rules
- verification thresholds
"""

from pathlib import Path

# Visible staging directory on Desktop
STAGING_DIR = Path.home() / "Desktop" / "STAGING"

# iCloud backup destination
ICLOUD_BACKUP_ROOT = (
    Path.home()
    / "Library"
    / "Mobile Documents"
    / "com~apple~CloudDocs"
    / "Z_Logic_Back_Ups"
)

# Retention policy
MAX_BACKUPS = 1

# Learned baseline threshold %
BASELINE_THRESHOLD = 0.70

BACKUP_SOURCES = [
    {
        "name": "components",
        "source": Path("/Library/Audio/Plug-Ins/Components"),
        "zip_name": "components.zip",
        "required": True,
    },
    {
        "name": "vst3",
        "source": Path("/Library/Audio/Plug-Ins/VST3"),
        "zip_name": "vst3.zip",
        "required": True,
    },
    {
        "name": "wpapi",
        "source": Path("/Library/Audio/Plug-Ins/WPAPI"),
        "zip_name": "wpapi.zip",
        "required": True,
    },
    {
        "name": "channel_strip_settings",
        "source": Path.home() / "Music" / "Audio Music Apps" / "Channel Strip Settings",
        "zip_name": "channel_strip_settings.zip",
        "required": True,
    },
    {
        "name": "plugin_presets",
        "source": Path.home() / "Music" / "Audio Music Apps" / "Plug-In Settings",
        "zip_name": "plugin_presets.zip",
        "required": True,
    },
    {
        "name": "sampler_instruments",
        "source": Path.home() / "Music" / "Audio Music Apps" / "Sampler Instruments",
        "zip_name": "sampler_instruments.zip",
        "required": True,
    },
    {
        "name": "patches",
        "source": Path.home() / "Music" / "Audio Music Apps" / "Patches",
        "zip_name": "patches.zip",
        "required": True,
    },
    {
        "name": "project_templates",
        "source": Path.home() / "Music" / "Audio Music Apps" / "Project Templates",
        "zip_name": "project_templates.zip",
        "required": False,
    },
]