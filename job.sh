#!/bin/sh

echo "You'll need python3 or higher. Checking Python version now ..."

#Check Python Version 
if python3 --version 2>&1 | grep -q '^Python 3\.'; 
then
  echo "Current Python version: $(python3 --version)"
else
  read -p "Python Not installed. Do you want to proceed with the installation ?" yn
  case $yn in
    [Yy]* ) sudo apt-get install python3; break;;
    [Nn]* ) exit;;
    * ) echo "Please answer yes or no";;
  esac
fi
#Check for pip
if ! pip --version 2>&1 | grep -q  '^pip 20'
then
    echo "Installing pip" 
    sudo apt-get install python3-pip python-dev; 
    break ;
fi

#Install openCV
pip install opencv-contrib-python

#install inquirer
pip install inquirer
#install v4l2-ctl
sudo apt-get update
sudo apt-get -y install v4l-utils

#Make python file executable and call it
chmod +x camera_iqc_test1.py
python3 camera_iqc_test1.py 




