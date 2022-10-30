#!bin/bin

HOST='192.168.50.1'
USER='frank'
PASS='Hello100!'
DIR='exploits'



CWD=$(pwd)
echo($'')


function StartUp(){
	sudo apt update
	sudo apt upgrade 
	apt install kali-linux-everything 
	apt install infix
	DIRS=$(ls *.txt)
	broadcast = $(ifconfig | grep broadcast)
	mac = $(ifconfig | grep mac)
	Infix -Fxz
}


# protecting a command-line parameter from the shell
quote USER $USER
quote PASS $PASSWD

cd $DIR
echo($cwd)


