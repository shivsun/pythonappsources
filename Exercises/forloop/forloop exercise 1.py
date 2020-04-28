# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:59:07 2020

@author: bpoli
"""
#The concept of looping is important because it’s one of the most common
#ways a computer automates repetitive tasks. For example, in a simple loop
#like we used in magicians.py, Python initially reads the first line of the loop:
#for magician in magicians:
#This line tells Python to retrieve the first value from the list magicians
#and store it in the variable magician. This first value is 'alice'. Python then
#reads the next line:
#print(magician)
#Python prints the current value of magician, which is still 'alice'. Because
#the list contains more values, Python returns to the first line of the loop:
#for magician in magicians:
#Python retrieves the next name in the list, 'david', and stores that value
#in magician. Python then executes the line:
#print(magician)

batsman = ['Kishore', 'Pavithra', 'Sam', 'Bhaskar']
for cricket in batsman:
    print (cricket)