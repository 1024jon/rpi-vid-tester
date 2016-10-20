# rpi-vid-tester
Interface for RPi touchscreen to output test video content using omxplayer over the HDMI output.

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
	sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev python-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python-dev
	sudo pip install -I Cython==0.23
	sudo pip install git+https://github.com/kivy/kivy.git@master
	
	nano ~/.kivy/config.ini
	ADD UNDER [INPUT]:
	mouse = mouse
	mtdev_%(name)s = probesysfs,provider=mtdev
	hid_%(name)s = probesysfs,provider=hidinput

