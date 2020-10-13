#! /bin/bash
cd ~/;
n=0

while [ $n -ne 5 ]
do
  clear;
	echo "1. Install Python3 2. Install pip3  3. Install Redis, RQ  4. Install Everything  5. Exit"
	echo "Input: "
	read n
	if [ $n -eq 1 ]
	then
		sudo apt-get install python3;
    python3 --version
		echo "Press Enter to Continue";
    read enter;
	elif [ $n -eq 2 ]
	then
		sudo apt-get install python3-pip;
		echo "Press Enter to Continue";
    read enter;
	elif [ $n -eq 3 ]
	then
    sudo apt-get update;
    sudo apt-get upgrade;
    sudo apt-get install redis-server;
    redis-server --version;
    sudo pip3 install rq;
		echo "Press Enter to Continue";
    read enter;
	elif [ $n -eq 4 ]
	then
    sudo apt-get install python3;
		sudo apt-get install python3-pip;
    sudo apt-get update;
    sudo apt-get upgrade;
    sudo apt-get install redis-server;
    sudo pip3 install rq;
    python3 --version;
    redis-server --version;
		echo "Press Enter to Continue";
    read enter;
	elif [ $n -gt 5 -o $n -lt 1 ]
	then
		echo "Invalid Input!"
		echo "Press Enter to Continue";
    read enter;
	else
		echo "Exiting Prgram"
	fi
done
