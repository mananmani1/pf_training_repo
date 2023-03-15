
function modify {
# Prompt the user to enter the directory path to be monitored

	echo "Enter the directory path to be monitored:"

	read data

# Check if the directory exists

	if [ ! -d "$data" ]; then

		echo "Error: Directory '$data' does not exist"

		exit 1

	fi

# Monitor the directory for changes using inotifywait

	echo "Monitoring directory '$data' for changes..."

	while show=$(inotifywait -e modify,create,delete,move $data);do

		echo "Directory '$data' has been $show "
		#cp ./$show ./output
	
	
	done
}
modify
	
	#output
	#  ./modify.sh
# Enter the directory path to be monitored:
# logs
# Monitoring directory 'logs' for changes...
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ DELETE log_1.txt:Zone.Identifier
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ DELETE log_2.txt:Zone.Identifier
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ DELETE log_3.txt:Zone.Identifier
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ DELETE log_4.txt:Zone.Identifier
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ DELETE log_5.txt:Zone.Identifier
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ MODIFY log_5.txt
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ CREATE New Text Document.txt
# Setting up watches.
# Watches established.
# Directory 'logs' has been logs/ MOVED_FROM New Text Document.txt
# Setting up watches.
# Watches established.
	

