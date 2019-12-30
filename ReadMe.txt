To add the script as a service:
	Modify ReceiveLights.service so that the python scripts path is in the ExecSTart line. By default, this points to a folder on the desktop
	Copy the file into /etc/systemd/system as root. EX: sudo cp ReceiveLights.service /etc/systemd/system/ReceiveLights.service

To start the service:	sudo systemctl start ReceiveLights.service
To stop the service:	sudo systemctl stop ReceiveLights.service
Get status of Service:	sudo systemctl status ReceiveLights.service

To set service to start at boot: sudo systemctl enable ReceiveLights.service
To stop service starting at boot: sudo systemctl disable ReceiveLights.service
