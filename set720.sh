#!/bin/bash

tvservice -d /home/pi/edid.dat
edidparser edid.dat > edid.txt