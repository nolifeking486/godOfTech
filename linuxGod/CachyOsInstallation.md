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


## Audio Enhancements for built in speakers
* using Easyeffects
```
sudo pacman -S easyeffects
sudo pacman -S lsp-plugins-lv2
sudo pacman -S zam-plugins
sudo pacman -S calf
sudo pacman -S mda.lv2
```

## Shelly
* just configure, already installed

## Important packages
* Intellij
* Brave : change settings and import bookmarks
* Telegram
* Qbittorent

## Git
* clone using ssh or later set url of repo to ssh one
```
git remote set-url origin git@github.com:username/repository.git
```
* generate ssh key `ssh-keygen -t ed25519 -C "your_email@example.com"
`
* check the key `cat ~/.ssh/id_ed25519.pub`
* add to Github


## Todo next
* Kde customization
* text editor
* make note of folder system
* remove cachyos bloat

## Skipping for now
* Easyeffects configuration
* clean D drive
* file naming -> no spaces
* wifi perma fix `echo "options iwlwifi power_save=0" | sudo tee /etc/modprobe.d/iwlwifi.conf`



# Late Game
## Mouse key customization
## Hyprland Ricing
## OBS


