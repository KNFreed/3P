#!/bin/bash
# Install Script for the 3P Console
# Updates everything
sudo apt-get update --yes --force-yes
sudo apt-get upgrade --yes --force-yes
sudo apt install --yes --force-yes \
    git \
    matchbox-keyboard \
# Install needed libraries
sudo pip3 install pillow
sudo pip3 install wifi
sudo pip3 install GitPython
sudo apt install python3-tk
