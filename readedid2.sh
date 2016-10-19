#!/bin/bash

touch /home/pi/edid.txt /home/pi/edid1.txt /home/pi/edid2.txt
tvservice -d /home/pi/edid.dat
edidparser /home/pi/edid.dat > /home/pi/edid.txt
tail -n 30 /home/pi/edid.txt > /home/pi/edid2.txt