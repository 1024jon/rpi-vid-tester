#!/bin/bash

tvservice -d /home/pi/edid.dat
edidparser /home/pi/edid.dat > /home/pi/edid.txt