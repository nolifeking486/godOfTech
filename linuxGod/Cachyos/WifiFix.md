# Fixing Intel Wireless-AC 9560 Disconnects on Linux (ASUS TUF FX505GE)


## The Symptoms
* Wi-Fi disappears completely after the laptop wakes from sleep or idle.
* `rfkill list` returns empty (wireless radio is completely unregistered by the kernel).
* `ip link` shows no `wlan0` or `wlo1` interfaces.
* The physical hardware is stuck in a frozen, low-power state across soft reboots.

## Step 1: Diagnose the Firmware Timeout
Verify that the kernel is failing to initialize the firmware due to a timeout. 

```bash
sudo dmesg | grep -iE "iwlwifi|iwlmvm|firmware" | tail -n 25
```
*Look for the error:* `Failed to start INIT ucode: -110` *(ETIMEDOUT)*.

## Step 2: Lock Kernel Module Power States
By default, the kernel driver allows low-power states which causes the Intel 9560 hardware to hang on the motherboard's CNVi bus upon waking up. We need to lock the kernel module to keep power active.

```bash
echo "options iwlwifi power_save=0" | sudo tee /etc/modprobe.d/iwlwifi.conf
echo "options iwlmvm power_scheme=1" | sudo tee /etc/modprobe.d/iwlmvm.conf
```

## Step 3: Disable NetworkManager Power Saving
Even with the kernel driver locked, NetworkManager (the desktop network daemon) will still try to force the card to sleep. Create a drop-in override configuration to strictly disable this behavior (`wifi.powersave = 2`).

```bash
sudo mkdir -p /etc/NetworkManager/conf.d/ #if directory not exist
printf "[connection]\nwifi.powersave = 2\n" | sudo tee /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
```

## Step 4: The Cold Embedded Controller (EC) Discharge
Because the Intel 9560 shares clock lines directly with the motherboard chipset, a normal reboot will not cut the residual standby voltage required to clear the frozen `-110` firmware state. You must physically drain the board's power.

1. Shut down the system completely: `sudo poweroff`
2. **Unplug the AC power adapter / charger** from the laptop.
3. Wait until all keyboard backlights and power LEDs are completely unlit.
4. **Press and hold the physical Power button for 40 to 60 seconds.**
5. Release the button, plug the charger back in, and turn the laptop on normally.

## Step 5: Verification
Once booted back to the desktop, confirm the interface is up and the configurations hold.

Check that the wireless interface is recognized again:
```bash
ip link
```

Check that power-saving is permanently disabled at the kernel driver level:
```bash
cat /sys/module/iwlwifi/parameters/power_save
```
*(Expected output: `0` or `N`)*