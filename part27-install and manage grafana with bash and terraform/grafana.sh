#!/bin/bash

####################################


sudo apt update 1> /dev/null
if [ $? -eq 0 ];then 
      	echo "################### repository updated ###################################"
else
	echo "################### Failed to update repository ##########################"
	exit 1
fi
####################################

wget -q -O - https://packages.grafana.com/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/grafana.gpg > /dev/null

if [ $? -eq 0 ];then
	echo "################### gpg add ############################## "
else
	echo "################### Failed to add gpg  ##################### "
	exit1
fi


####################################

echo "deb [signed-by=/usr/share/keyrings/grafana.gpg] https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

if [ $? -eq 0 ];then
	echo "################## add grafana repository ################ "
else
	echo "################## Faiied to add grafana repository ######################### "
	exit 1
fi

####################################

sudo apt-get install grafana

if [ $? -eq 0 ];then
	echo "################## install grafana ######################### "
else
	echo "##################  failed to install grafana ######################### "
	exit 1
fi
####################################
sudo systemctl start grafana-server
sudo systemctl enable grafana-server

 if [ $? -eq 0 ];then
	 echo "################# grafana-server enabled ########################### "
else
         echo "################# Failed to enable grafana-server ################# "
	 exit 1
 fi

#####################################

sudo ufw allow  3000 

if [ $? -eq 0 ];then
	echo "############### firewall open port 3000 ###############################"
else
	echo "############### failed to open port 3000 on firewall ################# "
	exit1
fi


###################################
echo "open port 3000"
echo "enjoy it ! "








































