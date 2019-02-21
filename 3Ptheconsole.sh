# Install Script for the 3P Console
# Updates everything
sudo sapt-get update && apt-get upgrade -y
# Install useful packages
sudo apt-get install matchbox-keyboard -y
# Install needed libraries
sudo pip3 install pillow
sudo pip3 install wifi
sudo pip3 install GitPython
