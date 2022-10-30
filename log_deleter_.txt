#!/usr/bin/env bash



function update_sys(){
	sudo apt update
	sudo apt upgrade 
	sudo apt dist-upgrade
}


function clear_dirs(){
echo "script to remove old files
"
	rm -R /var/log/

	folder_path=/home/pi/test/

	log_of_files=/var/log/

	date >> $log_of_files

	echo "---" >> $log_of_files

	find $folder_path -mtime +31 -name "*.log" >> $log_of_files

	find $folder_path -mtime +31 -name "*.log" -delete

	echo "--- " >> $log_of_files



}
update_sys
clear_dirs


# geektechstuff


