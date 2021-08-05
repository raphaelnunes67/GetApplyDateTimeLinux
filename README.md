# GetApplyDateTimeLinux
In this repository you will find a little python script to consult the date and time data on the web and 
apply them to the linux system.

This script was used in a Rasberry Pi Zero W which had a constant internet connection.

I followed the steps described below to run this script every startup:

- sudo cp -i /path/to/auto_date_time.py /bin
- sudo crontab -e
- open the file and go to a new line (without "#")
- add the command: "@reboot python3 /bin/auto_date_time.py &" (Don't forget the "&")
- test it using "sudo reboot"
