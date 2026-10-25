obviously without cable

## Using Python Server

for devices on same network only:

* cd to the required folder
* start server on a port `python3 -m http.server 8000`
* allow firewall access : `sudo ufw allow 8000/tcp`
* check server is working : `curl -I http://localhost:8000`
* go to the link in other device : `http://<ipaddress>:8000`
* do the needful
* close the server
* remove access from firewall : `sudo ufw delete allow 8000/tcp`

## Using ADB

**Prerequisite:** `sudo pacman -S android-tools`

### Pair (One-time setup)

1. On Android: **Developer Options > Wireless debugging > Pair device with pairing code**.
2. On PC: `adb pair <IP>:<Pairing-Port>` then enter Pairing code

### Connection

* Go back to Wireless debugging screen :`adb connect <IP>:<Connection-Port>`
* `adb push /local/path/to/folder /sdcard/Movies/FolderName`
* `adb disconnect`
* Wireless debugging off
