# rpi-vid-tester
Interface for RPi touchscreen to output test video content over the HDMI.  Planning to use omxplayer to output test files and change the HDMI output resolution using a touch interface.

Setup:
-----

	sudo nano /boot/config.txt
	UNCOMMENT:
		disable_overscan=1
		hdmi_force_hotplug=1
		hdmi_group=1
		hdmi_mode=4
	
	sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y && sudo reboot
	sudo apt-get -y install build-essential python-dev python-pip python-pygame git omxplayer