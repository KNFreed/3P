# Install Script for the 3P Console

# Updates everything
apt-get update && apt-get upgrade -y

# Install useful packages
apt-get install matchbox-keyboard -y

# Install needed libraries

sudo pip3 install pillow --update
sudo pip3 install wifi
