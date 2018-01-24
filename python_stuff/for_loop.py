#!/bin/python




for x in range(0,3):
	print "We are on time %d" %x

f = open('/etc/ansible/hosts', 'r')
for line in f:
	print(line) 
f.close()
