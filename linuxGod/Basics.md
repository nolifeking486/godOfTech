# Directory Structure
| Directory | Full Name | Purpose |
| :--- | :--- | :--- |
| **`/`** | Root | The absolute top of the filesystem hierarchy. |
| **`/home`** | Home | User personal files, configs, and desktop directories (e.g., `/home/username`). |
| **`/root`** | Root Home | The dedicated home directory for the superuser (root). |
| **`/bin`** | Binaries | Essential user command binaries (e.g., `ls`, `cp`, `ping`, `bash`). |
| **`/sbin`** | System Binaries | Administrative binaries strictly meant for root/system repair (e.g., `fdisk`, `reboot`). |
| **`/etc`** | Editable Text Configs | System-wide configuration files and startup scripts (e.g., `/etc/hosts`, `/etc/nginx`). |
| **`/var`** | Variable | Constantly changing data like log files (`/var/log`), mail spools, and databases. |
| **`/tmp`** | Temporary | Temporary files created by apps; usually cleared automatically on reboot. |
| **`/usr`** | User System Resources | Secondary hierarchy containing user utilities, libraries, and applications (`/usr/bin`, `/usr/lib`). |
| **`/opt`** | Optional | Third-party standalone software packages (e.g., Google Chrome, Discord). |
| **`/dev`** | Devices | Special device files representing hardware (e.g., `/dev/sda` for drives, `/dev/null`). |
| **`/proc`** | Processes | Virtual filesystem providing real-time kernel and process information. |
| **`/sys`** | System | Virtual filesystem exposing kernel settings and hardware parameters. |
| **`/media`** | Removable Media | Auto-mount point for removable media like USB sticks or CDs. |
| **`/mnt`** | Mount | Temporary mount point for filesystems mounted manually by administrators. |