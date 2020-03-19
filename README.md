# gpslogger
This is a python3 GPS logger code for use on a Raspberry Pi Zero.
It requires a GPS unit attached to the ttyS0 or serial0 port.

For it to work:
 - make sure all relevant libraries/packages are installed
 - place this script in /home/pi
 - create a folder in /home/pi called data

The script requires the gpsd service daemon installed on the RPiz
https://gpsd.gitlab.io/gpsd/index.html

Good instructions for installing GPSD are here: https://ozzmaker.com/berrygps-setup-guide-raspberry-pi/

Also required is the gpsd-py3 package as an interface to gpsd - https://github.com/MartijnBraam/gpsd-py3
 -- pip3 install gpsd-py3
