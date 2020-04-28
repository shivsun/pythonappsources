# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:06:27 2020

@author: bpoli
"""


#Accessing Elements in a List
#Lists are ordered collections, so you can access any element in a list by
#telling Python the position, or index, of the item desired. To access an element
#in a list, write the name of the list followed by the index of the item
#enclosed in square brackets.
#For example, let’s pull out the first bicycle in the list bicycles:

bikes = ["Royal Enfield", "Rajdoot", "Bajaj Chetak", "TVS Super"]

print (bikes[3].title())
print (bikes[2])
print (bikes [-1])

#Python has a special syntax for accessing the last element in a list. By asking
#for the item at index -1, Python always returns the last item in the list: