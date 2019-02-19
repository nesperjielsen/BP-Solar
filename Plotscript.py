# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:18:07 2019
@author: jespe
"""
### Reading output from MERCURY (.aei files) and plotting them
data = [[] for x in range(7*8)]
filenames = ["MERCURY.aei","VENUS.aei","EARTH.aei","MARS.aei","JUPITER.aei","SATURN.aei","URANUS.aei","NEPTUNE.aei"]
for f in filenames:
    with open(f, "r") as file:
        next(file)
        next(file)
        next(file)
        next(file)
        
        i = filenames.index(f)*7
        for line in file:
                data[i].append(float(line[4:19]))
                data[i+1].append(float(line[22:28]))
                data[i+2].append(float(line[29:37]))
                data[i+3].append(float(line[38:46]))
                data[i+4].append(float(line[47:55]))
                data[i+5].append(float(line[56:64]))
                data[i+6].append(float(line[65:73]))
#import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
#datalist = [2, 9, 16, 23, 30, 37, 44, 51]
#animation

'''
import matplotlib.animation as animation
fig, axarray = plt.subplots(1,2, figsize = (20,10))
plot1 = axarray[0]
plot2 = axarray[1]
mercury, = plot1.plot([],[],marker = ".",linestyle = " ", color = "brown", label = "Mercury")
venus, = plot1.plot([], [],marker = ".",linestyle = " ", color = "yellow", label = "Venus")
earth, = plot1.plot([],[],marker = ".",linestyle = " ", color = "blue", label = "Earth")
mars, = plot1.plot([],[],marker = ".",linestyle = " ", color = "red", label = "Mars")
plot1.plot(0,0, marker = "o", color = "black", label = "Sun", linestyle = "")
plot1.axis("equal")
plot1.set_title("The orbits of the four inner planets")
#plot1.tick_params(labeltop = True, labelright = True)
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
plot2.set_title("The orbits of the four outer planets")
plot2.set_xlim([-35,35])
plot2.set_ylim([-35,35])
plot2.set_xlabel("x [AU]")
plot2.set_ylabel("y [AU]")
#plot2.tick_params(labeltop = True, labelright = True)
text2 = plot2.text(-10,-30, "Yr", horizontalalignment = "right")
def animate(i):
    
    mercury.set_data(data[2][:i+1],data[3][:i+1])
    venus.set_data(data[9][:i+1],data[10][:i+1])
    earth.set_data(data[16][:i+1],data[17][:i+1])
    mars.set_data(data[23][:i+1],data[24][:i+1])
    text1.set_text("{} Yr".format(data[0][i]))
    
    jupiter.set_data(data[30][:i+1],data[31][:i+1])
    saturn.set_data(data[37][:i+1],data[38][:i+1])    
    uranus.set_data(data[44][:i+1],data[45][:i+1])
    neptune.set_data(data[51][:i+1],data[52][:i+1])
    text2.set_text("{} Yr".format(data[0][i]))
    
    return mercury, venus, earth, mars, text1, jupiter, saturn, uranus, neptune, text2
ani = animation.FuncAnimation(fig, animate, frames = len(data[0]), interval = 20, blit = True)
plot1.legend(loc = 4)
plot2.legend(loc = 4)
Writer = animation.writers["ffmpeg"]
writer = Writer(fps = 15,metadata = dict(artist = "Me"), bitrate = 1800)
ani.save('solarsystemmovie.mp4', writer = writer)

#plot of e and a
'''
data_places = list(range(6,56,7))
for i in data_places:
    plt.figure(figsize = (20,10))
    plt.plot(data[0], data[i] ,label = "{}".format(filenames[data_places.index(i)].split(".")[0]))

    plt.xlabel("Time (Yrs)")
    plt.ylabel("Eccentricity")
    plt.legend(loc = 3)
    plt.title("Evolution of eccentricity of {}".format(filenames[data_places.index(i)].split(".")[0]))


    plt.savefig("{}.png".format(filenames[data_places.index(i)].split(".")[0]))

data_places = list(range(2,24,7))
data_places1 = list(range(2,53,7))

fig, axarray = plt.subplots(1,2, figsize = (20,10))
plot1 = axarray[0]
plot2 = axarray[1]
points = 10000
for i in data_places:
    
    plot1.plot(data[i][:points],data[i+1][:points], label = "{}".format(filenames[data_places.index(i)].split(".")[0]), marker = ".", linestyle = " ")
    
for i in data_places1:
    plot2.plot(data[i][:points], data[i+1][:points], label = "{}".format(filenames[data_places1.index(i)].split(".")[0]), marker = ".", linestyle = " ")
    
plot1.plot(0,0, label = "SUN", marker = ".", linestyle = " ", color = "black")
plot2.plot(0,0, label = "SUN", marker = ".", linestyle = " ", color = "black")
fig.suptitle("Orbits of the planets in the Solar System")
fig.savefig("orbits.png")
plot1.legend(loc = 3)
plot1.set_xlabel("x (AU)")
plot1.set_ylabel("y (AU)")

plot2.set_xlabel("x (AU)")
plot2.set_ylabel("y (AU)")
plot2.legend(loc = 3)
plot1.text(0,-1.5, "Time elapsed: {} Yrs".format(data[0][points]))
plt.show()
