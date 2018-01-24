#!/bin/python

import itertools


mylist = [1,2,3,4,5,6,7,8,9]
#
#for i in mylist:
#	print i
#

k=2
#newlist=[]
#def printlists():
#	mylist = [1,2,3,4,5,6,7,8,9]
#	print int(len(mylist))
#	for i in mylist:
#		if len(mylist)  >  0 :
#			newlist.append(mylist[i])
#		        	
#			print newlist
#	return
#
#
#printlists()


#we want a list where we take ever 2 number and add it to the new list
#so we can take the first 2 number and add them to a new list 

def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

print chunks(mylist,2)
