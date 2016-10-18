# rpi-vid-tester
Interface for RPi touchscreen to output test video content over the HDMI.  Planning to use adafruit's pi_video_looper to output test files and change the HDMI output resolution using a touch interface

Setup:
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y && sudo reboot
git clone https://github.com/adafruit/pi_video_looper.git
cd pi_video_looper
sudo ./install.sh
sudo nano /boot/video_looper.ini
	CHANGE:
	file_reader = directory
	osd=false #leave true if needed for debugging
	path = /home/pi/Videos
