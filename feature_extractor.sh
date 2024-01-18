#!/bin/bash

echo "Activating shell script..."
# Activate the Python 2 virtual environment
# Please change the path to activate your environment
## /home/android/droidbox_env/bin/activate
source "$1"
echo "Activated virtual environment: $1"

# Check if the VIRTUAL_ENV variable is set
if [ -n "$VIRTUAL_ENV" ]; then
    echo "Virtual environment is activated: $VIRTUAL_ENV"
else
    echo "No virtual environment is currently activated."
fi

# Run the Python 2 script
# Please change the path to your tool destination and your
## /home/android/AndroPyTool/androPyTool.py
## /home/android/Desktop/Adware/
## test.csv
python "$2" -s "$3" -csv "$4" 
echo "Executed Python script with arguments: $2, $3, $4"

# Deactivate the virtual environment
deactivate
echo "Deactivated virtual environment"
