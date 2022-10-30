# sources=(
# 
# )
# 
# 
# 
# for src in "${sources[@]}"
# do
# 	git="git clone "
# 	echo"$src"
# 	git+=( "$src" )
# 	git
# done
# 
# printf '%s\n' "${destinations[@]}"


source=()
count = 0 
sudo -p
git="git clone "

while IFS= read -r line; do
   source+=("$line")
   #echo $source
   git+=("$source")
   
  localRepoDir=$(echo ${localCodeDir}${source}|cut -d'.' -f1)
  if [ -d $localRepoDir ]; then 	
  		echo -e "Directory $localRepoDir already exits, skipping ...\n"
	else 
		git_command="$git$source"
		echo "[$count] $git_command"
    	eval $git_command
		count=$(($count+1))
fi
	

done <sources.txt



# 
# 	if [ -d "./" ]; then 
# 		echo "dir exists."
# 		continue 
# 	fi 
# 	