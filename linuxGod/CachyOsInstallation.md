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
