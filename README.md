# 3P!: An Open Source Console working on Raspberry
![logo](https://raw.githubusercontent.com/KNFreed/3Ps-Stuff/master/logo.png)

# How to install the 3P!

** 1. Update everything and install Git **

```
sudo apt update; apt upgrade -y
sudo apt install git-core
```

** 2. Download the source files and execute the script **

```
cd /srv
sudo git clone https://github.com/KNFreed/3P
sudo chown -R $(whoami): 3P/
cd 3P
chmod a+x 3Ptheconsole.sh
./3Ptheconsole.sh
```
