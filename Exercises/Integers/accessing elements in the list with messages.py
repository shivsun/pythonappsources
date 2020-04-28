# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:09:17 2020

@author: bpoli
"""


#Accessing Elements in a List
#Lists are ordered collections, so you can access any element in a list by
#telling Python the position, or index, of the item desired. To access an element
#in a list, write the name of the list followed by the index of the item
#enclosed in square brackets.
#For example, let’s pull out the first bicycle in the list bicycles:

bikes = ["Royal Enfield", "Rajdoot", "Bajaj Chetak", "TVS Super"]
name = 'kishore'
name2 = 'vidya'
name3 = 'Sam'

print (bikes[3].title())
print (bikes[2])
print (bikes[-1])

message = "my first bike was " + bikes[2].title().upper() + "\t\nThen i bought" + bikes [0].lower()
message = "I have 2 friends, and both" + name.title() + "," + name2.title() + "comes to school on the bikes"

print (message + "They ride" + bikes[2]+ "," + bikes [0] + "respectively!") 

print (message)

#Python has a special syntax for accessing the last element in a list. By asking
#for the item at index -1, Python always returns the last item in the list:
#Tvs Super
#Bajaj Chetak
#TVS Super
#I have 2 friends, and bothKishore,Vidyacomes to school on the bikesThey rideBajaj Chetak,Royal Enfieldrespectively!
#I have 2 friends, and bothKishore,Vidyacomes to school on the bikes