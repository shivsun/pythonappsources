# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:16:28 2020

@author: bpoli
"""


bikes = ["Royal Enfield", "Rajdoot", "Bajaj Chetak", "TVS Super"]

bikes[2] = 'Luna'
bikes.remove("Rajdoot")
del bikes[1]
bikes.append("Pulser") 
bikes.insert(9, "Splender")
print (bikes)