#!/bin/bash
# Install Script for the 3P Console
# Updates everything
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt install -y matchbox-keyboard
# Install needed libraries
sudo pip3 install pillow
sudo pip3 install wifi
sudo pip3 install GitPython
sudo apt install -y python3-tk
