# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

data = [[] for x in range(8)]
with open("e_values.txt","r") as file:
	values = file.readlines()

for i in range(len(values)):
	for x in range(len(values[0].split(" "))-1):
		if values[i].split(" ")[x] == "ejected":
			data[x].append(values[i].split(" ")[x])
		else:
			data[x].append(float(values[i].split(" ")[x]))
name_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#Get Max values for all angles - need to be altered depending on amount of different angles and separations used
max_values = [[] for x in range(8)]
for i in range(len(name_list)):
	for x in range(len(data[i])/10):
		if all(e == "ejected" or "collided" for e in data[i][x*10:x*10+10]):
			break
		else:
			buffer = []
			for value in data[i][x*10:x*10+10]:
				if type(value) == float:
					buffer.append(value)
			max_values[i].append(np.mean(buffer))

for i in range(len(name_list)):
	start_value = 0.132
	step = 0.001
	stop_value = start_value+step*len(max_values[i])
	a_range = list(np.arange(start_value,stop_value,step))
	#a_range_correct = [x/0.005 for x in a_range]
	plt.plot(a_range,max_values[i], label = name_list[i], marker = 'x')

plt.title("Maximum eccentricity of the planets in the solar system \n during integrations of $10^5$ years")
plt.xlabel("Separation of binary (AU)")
plt.ylabel("Maximum eccentricity")
plt.xticks(a_range)
plt.legend()
plt.savefig("e_avg.png")
