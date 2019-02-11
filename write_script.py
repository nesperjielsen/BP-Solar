# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:00:12 2019

@author: jespe
"""
import numpy as np
lines = list(range(13,84,10))
i = 0
'''
data = []
with open("big.in", "r") as file:
    for line in file:
        if i in lines:
            data.append(line)
        i+=1    
print(data)
'''

with open("big.in", "r") as file:
    
    data = file.readlines()
    
for i in lines:
    data[i] = "{} \n".format(np.random.randint(0,360))

with open("big.in", "w") as file:
    file.writelines(data)



