#!/bin/bash

echo '*****************************************'
echo '*                                       *'
echo '*      Installation de la Raspberry     *'
echo '*                                       *'
echo '*****************************************'

#-----------------------------------------------
echo '	- Copy des fichiers'

mkdir $HOME/fichiers
cp rasp/skyetek.c $HOME/fichiers/skyetek.c
cp rasp/script.py $HOME/fichiers/script.py

#-----------------------------------------------
echo '	- Installation du script de démarrage'

sed -i -e "s/cd /home/pi/fichiers/
python /home/pi/fichiers/script.pi/cd \/home\/pi\/fichiers\/\npython \/home\/pi\/fichiers\/script.pi\nexit 0/g" /etc/rc.local

#-----------------------------------------------
echo '	- Installation des modules necessaires'
sudo apt-get update && sudo apt-get upgrade && sudo apt-get install -y mosquitto python-pip python-mysqldb

pip install paho-mqtt

echo '********** Installation terminée **********'

exit 0
