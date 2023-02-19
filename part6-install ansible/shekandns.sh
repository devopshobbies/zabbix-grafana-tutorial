#!/bin/bash
#author:amir.ajoodani@gmail.com
result="$?"
sed -i '2i nameserver 185.51.200.2' /etc/resolv.conf
if result=0;then
echo '185.51.200.2 Is Set '
else
echo '185.51.200.2 Is Not Set'
fi
sed -i '3i nameserver 178.22.122.100' /etc/resolv.conf
if result=0;then
echo '178.22.122.100 Is Set '
else
echo '178.22.122.100 Is Not Set'
fi
