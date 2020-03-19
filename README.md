# gpslogger
This is a python3 GPS logger code for use on a Raspberry Pi Zero.
It requires a GPS unit attached to the ttyS0 or serial0 port.

For it to work:
 - make sure all relevant libraries/packages are installed
 - place this script in /home/pi
 - create a folder in /home/pi called data

The script requires the gpsd service daemon installed on the RPiz
https://gpsd.gitlab.io/gpsd/index.html

and the gps3 package installed - https://pypi.org/project/gps3/
  pip3 install gps3
