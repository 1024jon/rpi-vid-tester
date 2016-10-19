#!/bin/bash

killall omxplayer.bin
sleep 2
omxplayer --nativedeinterlace -y --aspect-mode stretch --loop --display=5 /home/pi/rpi-vid-tester/testvids/general.mp4