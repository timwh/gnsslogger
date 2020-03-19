#!/usr/bin/env python3
# -------------------------------------------------------------------
# A data logger GPS on RPi zero W
# GPS connected to ttyS0 (serial0)
# Tim Whiteside
# For it to work:
#  - make sure all relevant libraries/packages are installed
#  - place this script in /home/pi
#  - create a folder in /home/pi called data
# -------------------------------------------------------------------
# LIBRARIES
# requires gpsd service daemon installed and running--- https://gpsd.gitlab.io/gpsd/index.html
# also requires the package gpsd-py3 installed as an interface to gpsd --- https://github.com/MartijnBraam/gpsd-py3
import gpsd
from time import strftime, sleep

# GLOBAL
timestr=strftime("%Y%m%d--%H%M%S-%Z")

# Function: Log file setup
def get_file_name():
    #use date and time to name file
    return "GPSlog_" + timestr + ".txt"
# Get full path for writing and set up headers
name = get_file_name()
path = "/home/pi/data/"+ name
with open(path,"w") as log:
    log.write("time,lat,long\n")

# Connect to the local gps daemon
gpsd.connect()

#Run loop
while True:
    packet = gpsd.get_current()  # poll GPS location
    if packet.mode >= 2:
        print("Time: " + str(packet.time), " Latitude: " + str(packet.lat), " Longitude: " + str(packet.lon), "  Mode: " + str(packet.mode),"Sats: " + str(packet.sats))
        # write to file
        with open(path, "a") as log:
            log.write("{0},{1},{2}\n".format(str(packet.time), str(packet.lat), str(packet.lon)))

    else:
        print("Waiting for a fix........")
        sleep(0.2)
 
        



