#!/usr/bin/env python


#.....########...#######...#######..########..########..##.....##..######..##.....##.....
#.....##.....##.##.....##.##.....##.##.....##.##.....##.##.....##.##....##.##.....##.....
#.....##.....##.##.....##.##.....##.##.....##.##.....##.##.....##.##.......##.....##.....
#.....##.....##.##.....##.##.....##.########..########..##.....##..######..#########.....
#.....##.....##.##.....##.##.....##.##...##...##........##.....##.......##.##.....##.....
#.....##.....##.##.....##.##.....##.##....##..##........##.....##.##....##.##.....##.....
#.....########...#######...#######..##.....##.##.........#######...######..##.....##.....

#	http://matthiasschaffer.com/dev/doorpush/


import nxt.locator
from nxt.sensor import *
import time
import requests

b = nxt.locator.find_one_brick(name = 'Boris')

print 'Touchsensor auf Port 1!'

#STARTUP TESTS
print 'Sensor Test:', Touch(b, PORT_1).get_sample()
print 'Push Test'
url = "API_URLS_ARE_PRIVATE_:("
r = requests.get(url)

press = 0

while True:
	
	if Touch(b, PORT_1).get_sample() == True:
			press = 1
	else:
	   if press == 1:
			press = 0
			url = "API_URLS_ARE_PRIVATE_:("
			r = requests.get(url)
			print 'Msg sent!'
	
	time.sleep(1)
