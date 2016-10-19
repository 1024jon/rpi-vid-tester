#!/bin/bash

killall omxplayer
omxplayer --nativedeinterlace -y --aspect-mode stretch --loop --display=5 /home/pi/rpi-vid-tester/testvids/overscancrop.m4v