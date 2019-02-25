# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:07:43 2019

@author: jespe
"""
import os
import write_script
import plotscript

#pseudo integrate the orbit of the binary and the planets

with open("param.in", "r") as file: #change the integration time to one step and change the central body mass
    
    lines = file.readlines()

lines[7] = " stop time (days) = 365.25d0"
sun_value = input("mass of central body: ")
lines[28] = " central mass (solar) = {}".format(sun_value)

with open("param.in", "w") as file:
    file.writelines(lines)
    
with open("big.in", "r") as file: #change a,e of companion
    
    lines = file.readlines()

sun_sma = input("semi-major axis: ")
sun_e = input("eccentricity: ")

lines[7] = sun_sma
lines[8] = sun_e

with open("big.in", "w") as file:
    
    file.writelines(lines)

write_script.write() #generate orbitals

os.system("./mercury6") #integrate
os.system("./element6") #create output files


#read output files, store them in big.in
filenames = ["SUN2.aei","MERCURY.aei","VENUS.aei","EARTH.aei","MARS.aei","JUPITER.aei","SATURN.aei","URANUS.aei","NEPTUNE.aei"]
data = [[] for x in range(9*9)]
for f in filenames:
    
    with open("f", "r") as file:
        
        next(file)
        next(file)
        next(file)
        next(file)
        
        i = filenames.index(f)*9
        for line in file:
                data[i+4].append(float(line[47:55]))
                data[i+5].append(float(line[56:64]))
                data[i+6].append(float(line[65:73]))
                data[i+7].append(float(line[74:82]))
                data[i+8].append(float(line[83:91]))
                data[i+9].append(float(line[92:100]))


with open("big.in", "r") as file:
    big_lines = file.readlines()

for i in range(7,65):
    if i in list(range(16,97,10)):
        continue
    if i in list(range(13, 104,10)):
        continue
    if i in list(range(14, 105, 10)):
        continue
    if i in list(range(15, 106, 10)):
        continue
    big_lines[i] = data[i-3][0]

with open("big.in", "w") as file:
    file.writelines(big_lines)

#Remove excess files
os.system("rm *.aei")
os.system("rm *mp")
os.system("rm *.out")

with open("param.in", "r") as file:
    
    lines = file.readlines()

lines[7] = " stop time (days) = 365.25d6"
with open("param.in", "w") as file:
    file.writelines(lines)

#integrate the planets and the suns
os.system("./mercury6")
os.system("./element6")

#ADD TO READ INFO.OUT TO CHECK FOR CLOSE ENCOUNTERS

'''
plotscript.i_e()
os.system("mv *.png BP-Solar")
os.system("mv *.aei BP-Solar")
os.system("mv big.in BP-Solar")
os.system("mv info.out BP-Solar")
os.system("cd BP-Solar")
os.system("git add .")
os.system("git commit -m \"Integration with {} separation\" ")
os.system("git push origin master")
'''



