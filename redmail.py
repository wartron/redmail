#configure your details here
user = "" #reddit username
password = "" #reddit password
delay = 60*5 #delay in seconds between checking mail

import time
import sys
import pywinusb.hid as hid
import reddit

def get_device():
	all_devices = hid.HidDeviceFilter(vendor_id = 0x1294).get_devices()
		if len(all_devices)==0:
		print "Can't find target device"		
	else:		
		return all_devices[0]
	return null
	
	
def set_color(device,color):
		for report in device.find_output_reports():
			if 4278190081 in report:
				report[4278190081] =  [color,0,0,0,0] 
				report.send() 				
	
				
if __name__ == '__main__':	
	try:
		d = get_device()
		d.open()
		
		set_color(d,0)
		r = reddit.Reddit(user_agent="redmail")
		r.login(user=user,password=password)
		inbox = r.get_inbox()
		
		while True:			
			new = inbox.get_new_messages(force=True)
			if len(new) > 0:
				set_color(d,2)
			else:
				set_color(d,0)				
				
			time.sleep(delay)
		
	finally:
		d.close()

	exit()