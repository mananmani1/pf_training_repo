
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

	while true; do

		inotifywait -r -e modify,create,delete,move "$data"

		echo "Directory '$data' has been modified."
	
	
	done
}
modify
	
	

