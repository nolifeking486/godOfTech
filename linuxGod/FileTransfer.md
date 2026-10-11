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
