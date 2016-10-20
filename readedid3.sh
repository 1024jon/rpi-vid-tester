#!/bin/bash

touch /home/pi/edid.txt /home/pi/edid1.txt /home/pi/edid3.txt
tvservice -d /home/pi/edid.dat
edidparser /home/pi/edid.dat > /home/pi/edid.txt
sed -n '31,55p' < edid.txt > /home/pi/edid3.txt