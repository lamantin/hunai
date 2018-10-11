#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

if ! [ -x "$(command -v python)" ]; then
  echo 'Error: python is not installed.' >&2
  sudo apt-get install python-dev
  
fi

if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed.' >&2
  sudo apt-get install python-pip
  
fi

if ! [ -x "$(command -v mpg321)" ]; then
  echo 'Error: pip is not installed.' >&2
  sudo apt-get -y install mpg321
  
fi

# 

pip install -r requirements.txt