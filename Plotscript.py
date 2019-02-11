# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:18:07 2019

@author: jespe
"""
### Reading output from MERCURY (.aei files) and plotting them
data = [[] for x in range(6*8)]
filenames = ["MERCURY.aei","VENUS.aei","EARTH.aei","MARS.aei","JUPITER.aei","SATURN.aei","URANUS.aei","NEPTUNE.aei"]
for f in filenames:
    with open(f, "r") as file:
        next(file)
        next(file)
        next(file)
        next(file)
        
        i = filenames.index(f)*6
        for line in file:
                data[i].append(float(line[8:19]))
                data[i+1].append(float(line[22:28]))
                data[i+2].append(float(line[29:37]))
                data[i+3].append(float(line[38:46]))
                data[i+4].append(float(line[47:55]))
                data[i+5].append(float(line[56:64]))
                #data[i+6].append(float(line[65:73]))

import matplotlib.pyplot as plt
import matplotlib.animation as animation
#datalist = [2, 8, 14, 20, 26, 32, 38, 44]
fig, axarray = plt.subplots(1,2, figsize = (20,10))

plot1 = axarray[0]

plot2 = axarray[1]

mercury, = plot1.plot([],[],marker = ".",linestyle = " ", color = "brown", label = "Mercury")
venus, = plot1.plot([], [],marker = ".",linestyle = " ", color = "yellow", label = "Venus")
earth, = plot1.plot([],[],marker = ".",linestyle = " ", color = "blue", label = "Earth")
mars, = plot1.plot([],[],marker = ".",linestyle = " ", color = "red", label = "Mars")
plot1.plot(0,0, marker = "o", color = "black", label = "Sun", linestyle = "")
plot1.axis("equal")
plot1.set_xlim([-2,2])
plot1.set_ylim([-2,2])
plot1.set_xlabel("x [AU]")
plot1.set_ylabel("y [AU]")
text1 = plot1.text(-1,-1.5, "Yr", horizontalalignment = "right")


jupiter, = plot2.plot([],[], color = "brown", label = "Jupiter")
saturn, = plot2.plot([], [], color = "orange", label = "Saturn")
uranus, = plot2.plot([],[], color = "darkblue", label = "Uranus")
neptune, = plot2.plot([],[], color = "turquoise", label = "Neptune")
plot2.plot(0,0, marker = "o", color = "black", label = "Sun", linestyle ="")
plot2.axis("equal")
plot2.set_xlim([-35,35])
plot2.set_ylim([-35,35])
plot2.set_xlabel("x [AU]")
plot2.set_ylabel("y [AU]")
text2 = plot2.text(-10,-30, "Yr", horizontalalignment = "right")
def animate(i):
    mercury.set_data(data[2][:i+1],data[3][:i+1])
    venus.set_data(data[8][:i+1],data[9][:i+1])
    earth.set_data(data[14][:i+1],data[15][:i+1])
    mars.set_data(data[20][:i+1],data[21][:i+1])
    text1.set_text("{} Yr".format(data[0][i]))
    
    jupiter.set_data(data[26][:i+1],data[27][:i+1])
    saturn.set_data(data[32][:i+1],data[33][:i+1])    
    uranus.set_data(data[38][:i+1],data[39][:i+1])
    neptune.set_data(data[44][:i+1],data[45][:i+1])
    text2.set_text("{} Yr".format(data[0][i]))
    
    return mercury, venus, earth, mars, text1, jupiter, saturn, uranus, neptune, text2


ani = animation.FuncAnimation(fig, animate, frames = len(data[0]), interval = 20, blit = True)
plot1.legend(loc = 4)
plot2.legend(loc = 4)

Writer = animation.writers["ffmpeg"]
writer = Writer(fps = 15,metadata = dict(artist = "Me"), bitrate = 1800)
ani.save('solarsystemmovie.mp4', writer = writer)




    
    
