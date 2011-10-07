#configure your details here
user = "" #reddit username
password = "" #reddit password
delay = 60*5 #delay in seconds between checking mail

import time
import sys
import pywinusb.hid as hid
import reddit

def get_device(target_vendor_id):
	all_devices = hid.HidDeviceFilter(vendor_id = target_vendor_id).get_devices()
	
	if not all_devices:
		print "Can't find target device (vendor_id = 0x%04x)!" % target_vendor_id
	else:		
		return all_devices[0]
		
	return null
	
def set_color(device,color,target_usage):
		for report in device.find_output_reports():
			if target_usage in report:
				report[target_usage] =  [color,0,0,0,0] 
				report.send() 				

				
				
if __name__ == '__main__':
	target_vendor_id = 0x1294
	target_usage = hid.get_full_usage_id(0xff00, 0x0001)
	
	try:
		d = get_device(target_vendor_id)
		d.open()
		
		set_color(d,0,target_usage)
		r = reddit.Reddit(user_agent="redmail")
		r.login(user=user,password=password)
		inbox = r.get_inbox()
		
		while True:
			
			new = inbox.get_new_messages(force=True)
			if len(new) > 0:
				set_color(d,2,target_usage)
			else:
				set_color(d,0,target_usage)				
				
			time.sleep(delay)
		
	finally:
		d.close()

	exit()



