#!/bin/bash

tvservice -d /home/pi/edid.dat
edidparser /home/pi/edid.dat > /home/pi/edid.txt
head -20 /home/pi/edid.txt > /home/pi/edid1.txt