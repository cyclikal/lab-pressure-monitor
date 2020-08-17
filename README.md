# Lab Pressure Monitor
A short script for a Rasperry Pi Zero-powered data logger (measuring lab temperature and humidity, and glove box temperature, humidity, and pressure).

## General Use
This script will upload data to a Google Sheets document. The document name is currently "Lab Monitor Data" and should be shared with relevant users. Vincent and Aaron both have access to the Google API settings for the service account that runs on the Pi Zero W to upload data, although any Cyclikal Google user may have access (has not been verified yet).

## Setup
### Raspian
To setup from scratch, start with a fresh install of Raspbian Lite (no need for the full desktop as this will run headless). The microSD card should be at least 4GB in size. It's recommended to start with a [headless setup](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html) for easier interfacing.

Once connected (probably through SSH), use `sudo raspi-config` to:
- Enable the I2C interface
- Change the hostname to `lab-pressure-monitor` or something similar
- Reboot once done

Finally, follow these steps for the code:
- `sudo apt-get install git` as it may not be installed on Raspbian Lite by default
- Clone this repository to the pi home directory
- Move `lab_pressure_monitor.py`, `sensor_data.py`, and `check_wifi.sh` to the home directory

### Networking
Since the goal of this project is to run headless (continuously) for months at a time, it will be useful to have a script in place to ping a local IP and ensure that there is a network connection. To do this, follow these steps:
- Change the `GATEWAY` in `check_wifi.sh` to a local IP to ping (router maybe?) to check the WiFi connection
- Do `sudo chmod +x check_wifi.sh` to make the script executable
- Add to crontab with `crontab -e`, then add `*/10 * * * * sudo /home/pi/check_wifi.sh` to the end of the file. This will run the script every 10 minutes to check the local connection, and restarts wlan0 if it's down. Obviously, if the Pi keeps disconnecting, there's probably a bigger problem.

### Wiring and Physical Setup
This should already be done (unless it's been unplugged and moved or something), but the Pi should be connected to a 3D print witht the DHT22 sensor on it as well. That print clips on a wire breakout box that plugs into the back of the glove box, which runs inside the box to the Sparkfun BME280 board (small red PCB) on its own 3D printed bracket.

Check `sensor_data.py` for the DHT22 pin in case the header pins that plug into the Pi Zero have been broken. Otherwise, that header should have five connections ([pinout.xyz](https://www.pinout.xyz) is helpful here):
- 3V3 (red heatshrink)
- I2C for BME280 pressure sensor (yellow heatshrink)
- GND (black heatshrink)
- DHT22 pin (green heatshrink)

To find the 3D printed parts used for this, go to the cyclikal-cad-files repository and search for the relevant keywords (file names should be something like "pi_zero_enclosure" and "pressure_sensor_enclosure")

### Finally, _the actual code..._
For this to run, the Pi will use a Google service account to edit a spreadsheet. This is easier than other ways of authenticating since the Pi can be logged in forever (a slight security risk, but much simpler). To get the `service_account.json` file needed for operation, you will need to have access to the **"Lab Monitor Data"** Google Spreadsheet, and the **"Lab Monitor Project"** API project within the Google APIs & Services webpage.

Go to [this link](https://console.developers.google.com/apis/credentials?authuser=0&project=lab-monitor-project&supportedpurview=project) with a Cyclikal account to access the credentials page, click on the **"lab-monitor-account"** service account, and generate a new key with "ADD KEY" -> "Create new key" -> JSON. Then move this file into the pi's home directory. _It should be named `service_account.json`._ Before doing anything else, verify that the email listed in `service_account.json` has been given edit access to the data spreadsheet. If not, just give it access as if you were doing it for a human user.

Finally, set up `lab-pressure-monitor.py` to run on boot by **TODO: FINISH THIS**
