#! /bin/bash 


## FILE CONDITIONS ### 
# -d (True if is a directory)
# -e (true if file exists )
# -f (True if string is a filename)
# -g (True for group ID)
# -r (True if readable)
# -s (True if file is non 0 size)
# -u (True if the file is set)
# -w (True if file is wrtable)
# -x (true if exextuable)
#########



####### THE CUT COMMANDS ##### 
# -f, --fields	Field-based selection
# -d, --delimiter	Delimiter for field-based selection
# -c, --characters	Character-based selection, delimiter ignored or error
# -s, --only-delimited	Suppress lines with no delimiter characters (printed as-is otherwise)
# --complement	Inverted selection (extract all except specified fields/characters
# --output-delimiter	Specify when it has to be different from the input delimiter
# 
###### EXAMPLE ######
# cut -f1,3 # extract first and third tab-delimited field (from stdin)
# cut -f1-3 # extract from first up to third field (ends included)
# cut -f-3 # -3 is interpreted as 1-3
# cut -f2- # 2- is interpreted as from the second to the last
# cut -c1-5,10 # extract from stdin the characters in positions 1,2,3,4,5# ,10
# cut -s -f1 # suppress lines not containing delimiters
# cut --complement -f3 # (GNU cut only) extract all fields except the third
####### EXAMPLE ########



#vars 
name="l337"
FILE='text.txt'
DIR ="DIR"
M_NAMES="FRANK JESSIE GRIMES HOMER"


## FILE MANIPULATION 
if [-f "$FILE"]
then
	echo "${FILE} is indeed a file!"
else
	echo "Could not find ${FILE} :["
fi
	
	if [-d "$DIR"]
then
	echo "${DIR} is indeed a file!"
else
	echo "Could not find ${DIR} :["
fi
	
#### FOR LOOP TO MANIPULATE FILE ### 
DIRS=$(ls *.txt)
NEW="new"
for DIR in $DIRS 
	do 
		echo "renaming $DIR to new-$DIR"
		mv $DIR $NEW-$DIR 
	done 

### READ THROUGH LINE BY LINE 
LINE=1 
while read -r CURRENT_LINE 
	do
		echo "reading lines.. "
		echo "$LINE: $URRENT_LINE" 
		((LINE++))
	done < "./new-1.txt"
		
		
## CREATE FOLDER AND WRITE TO FILE 
mkdir hello
touch "hello/world.txt"
echo "hello world" >> "hello/world.txt"
echo "created hello world fioled in hello dir"
######

### to copy variable to new loc 
destdir=$(pwd)
    if [ -f "$destdir" ]
    then 
    echo "$var" > "$destdir"
    fi



### SIMPLE FUNCTION 
function hello_world(){
	echo "hello world"
}
hello_world

function say_hello(){
	echo "hello, i am $1, and i am $2"
}
say_hello "frankie" "33"

###########

	
	
## CASE-STATEMENT 
read -p "are you over 21 years old? Y/N" ANSWER 
case $"ANSWER" in 
	[yY] | [yY][eE][sS])
	echo "You can have a beer!"
	;; 
	[nN] | [nN][oO]) 
	echo "sorry no drinking" 
	;;
	*) 
	echo "please enter y/yes or n/no"
	;;
esac 



## TO SET COMMAND OUTPUT TO VAR
## var=$(/path/to/command)
## var=$(/path/to/command arg1 arg2)
### var=$(command-name-here)


## SIMPLE WHILE LOOP 
for S_NAME in $M_NAMES 
	do
	echo"hello, ${S_NAME}" 
done


### CREATE 4 PASSWORD 
for p in $(seq 1-4); 
do
  echo 'iterating...'
  openssl rand -base64 48 | cut -c1-$PASS_LEN # string traversal 
done 

#### TO REMOVE CHARICTER FROM STR 
### ( | sed 's/h//')

### displaying multiple items 
cat –e SampleFile1 SampleFile2



#### RUNNING MULTIPEL COMMANDS 
cd myfolder; ls   # no matter cd to myfolder successfully, run ls
cd myfolder && ls  # run ls only after cd to myfolder
cd myfolder || ls  # if failed cd to myfolder, `ls` will run
##






#Print 
echo hello world! 
echo "my name is ${name}"

#User-Input 
read -p "Enter your real name " NAME 
echo "so your real name is, ${NAME}? or ${name}" 
read -p "1 for former, 2 for latter" decision


# conditionals 
if [ -z "$decision" ]; ## if var is empty
then
	echo "\$decision is empty... i need to know your name!"
	echo "Please tell me your name.. "
	read real_name 
	echo "nice to meet you, ${real_name}"
if ["$decision" == 1]	
	echo "pleasure to meet you, ${name}"
else 
	echo "your aquantence, ${NAME} is becomming of my existance. thank you so much."
fi


