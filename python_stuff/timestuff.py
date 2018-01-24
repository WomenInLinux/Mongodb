#!/bin/python3.6

import time

start_time = time.localtime()
print("Timer start at %s" % time.strftime( "%X" , start_time))

#Wait for user input

input("Please press enter to continue...")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)
print("Time stopped at %s" % time.strftime( "%X" , stop_time))
print("Total time: %s seconds" %difference)
