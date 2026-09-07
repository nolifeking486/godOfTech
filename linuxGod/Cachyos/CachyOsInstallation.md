# Pre-Installation
* **Data Backup** : users, browser, git repos commit changes


* **Bootable Usb** : use rufus with GPT,UEFI rest default

## Bios
*   **Secure Boot:** `Disabled`
*   **Fast Boot:** `Disabled`
*   **Boot Priority #1:** `USB Drive`


## Bypassing the Intel CNVi Wi-Fi Bug (Pre-Install Workaround)
* **The Problem:** Windows crashing leaves the Intel Wi-Fi chip in a "zombie" state. The CachyOS live USB cannot detect the Wi-Fi hardware, preventing the net-installer from running.  
* **Workaround:** USB tethering/Ethernet

## Installer
* just go next next
---

# Post Install
## System Verification
Run these commands in the terminal to verify hardware integration:
*   `sudo pacman -Syu` (Update core system).
*   `nvidia-smi` (Verify Wayland is using proprietary NVIDIA drivers).
*   `zramctl` (Verify ZRAM memory compression is active).

## BTRFS Snapshots
* just verify defaults and change number of saves to 10

## Firewall
* default enabled
* open Firewall and change incoming default to deny

## Heat Management
* thermald (Intel)
* install ` sudo pacman -S thermald`
* start `sudo systemctl enable --now thermald.service `
* check running properly `systemctl status thermald.service` and `journalctl -u thermald.service -b`

## Fix Display Scaling
* display settings -> scaling

##  Auto-Mounting the Internal HDD
By default, Linux requires root passwords to access internal drives. To automate this:
1. Install GNOME Disks: `sudo pacman -S gnome-disk-utility`
2. Open Disks, select the HDD, and click the specific partition block.
3. Click the gear icon (⚙️) -> **Edit Mount Options...**
4. Toggle off **User Session Defaults**.
5. Ensure **Mount at system startup** is checked.
6. Save and reboot.

## Claim the drive
* find exact user: `whoami`
* path where drive is mounted : `df -h` copy it
* run `sudo chown -R user:user /path/to/your/hdd`

## Asus built in Keyboard configure
* `asusctl` : cli based manager

## Audio Enhancements for built in speakers
* using Easyeffects
```
sudo pacman -S easyeffects
sudo pacman -S lsp-plugins-lv2
sudo pacman -S zam-plugins
sudo pacman -S calf
sudo pacman -S mda.lv2
```
## Battery
* fix max charging level to `80%` in KDE Advanced Settings


## Important packages and remarks
* Shelly: GUI package manager
* Intellij: IDE
* Brave : change settings and import bookmarks
* Telegram
* Qbittorent
* Kitty: Terminal
* Cliamp: Youtube Music client


## Git
* clone using ssh or later set url of repo to ssh one
```
git remote set-url origin git@github.com:username/repository.git
```
* generate ssh key `ssh-keygen -t ed25519 -C "your_email@example.com"
`
* check the key `cat ~/.ssh/id_ed25519.pub`
* add to Github

---
# How to Offload XDG Media Folders to HDD

This guide covers moving default Linux media folders to a secondary HDD while keeping the system, web browsers, and legacy apps functioning perfectly.
* **NOTE** : change "/mnt/hdd" to actual path
## 1. Create Target Folders on HDD
```bash
mkdir -p /mnt/hdd/linux-media/{Downloads,Music,Pictures,Videos,Documents}
```

## 2. Move Existing Data
Move contents from the SSD to the HDD (ignore any "No matches for wildcard" errors if the folder is empty).
```bash
mv ~/Downloads/* /mnt/hdd/linux-media/Downloads/ 2>/dev/null
mv ~/Music/* /mnt/hdd/linux-media/Music/ 2>/dev/null
mv ~/Pictures/* /mnt/hdd/linux-media/Pictures/ 2>/dev/null
mv ~/Videos/* /mnt/hdd/linux-media/Videos/ 2>/dev/null
mv ~/Documents/* /mnt/hdd/linux-media/Documents/ 2>/dev/null
```

## 3. Update XDG Configuration
Update the system's XDG path configuration to natively use the HDD.
```bash
nano ~/.config/user-dirs.dirs
```
Update the variables inside:
```text
XDG_DOCUMENTS_DIR="/mnt/hdd/linux-media/Documents"
XDG_DOWNLOAD_DIR="/mnt/hdd/linux-media/Downloads"
XDG_MUSIC_DIR="/mnt/hdd/linux-media/Music"
XDG_PICTURES_DIR="/mnt/hdd/linux-media/Pictures"
XDG_VIDEOS_DIR="/mnt/hdd/linux-media/Videos"
```

## 4. Delete Old Folders
Remove the now-empty directories from your home folder.
```bash
rmdir ~/Downloads ~/Music ~/Pictures ~/Videos ~/Documents
```

## 5. Create Symlinks (The Fallback)
Create symlinks pointing back to `$HOME` so legacy apps don't accidentally create new folders on the SSD.
```bash
ln -s /mnt/hdd/linux-media/Downloads ~/Downloads
ln -s /mnt/hdd/linux-media/Music ~/Music
ln -s /mnt/hdd/linux-media/Pictures ~/Pictures
ln -s /mnt/hdd/linux-media/Videos ~/Videos
ln -s /mnt/hdd/linux-media/Documents ~/Documents
```

**To verify the symlinks worked:**
```bash
ls -la ~ | grep -- "->"
```

---
## Todo next
* text editor -> configure and learn Neovim or Lazyvim

## Skipping for now
* Easyeffects configuration
* clean D drive
* file naming -> no spaces



# Late Game
* Mouse key customization
* Hyprland Ricing
* OBS


