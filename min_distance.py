import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
import numpy as np
abin = [0.13,0.135,0.14,0.145,0.15,0.155,0.16]
#abin = [0.3,0.32,0.34,0.36,0.38,0.4]
#abin = [0.42,0.44,0.46,0.48,0.5,0.52,0.54]
m_ven = 2.4478383396645447*10**-6
r_hill = 0.72333*(1+0.00678)*(m_ven/3.0)**(1/3)
rmin = [[]]
for sun_sma in abin:
	if os.path.isfile("a{}/rmin.txt".format(sun_sma)):
		with open("a{}/rmin.txt".format(sun_sma),"r") as file:
			for line in file:
				rmin[abin.index(sun_sma)].append(line.split("\n")[0])
	rmin.append([])
fig, axes = plt.subplots()
for x,y in zip(abin,rmin):
	plt.scatter([x]*len(y),y,color = "black")
axes.tick_params(top = True, bottom = True, left = True, right = True)
plt.hlines(r_hill, xmin = min(abin),xmax = max(abin), label = "largest Hill sphere of Venus")
plt.xlabel("Binary separation (AU)")
plt.ylabel("Minimum distance (AU)")
plt.yscale("log")
plt.xlim(right = 0.165,left = 0.125)
plt.ylim(bottom = 0.001)
plt.title("Minimum distance between Mercury and Venus \n for all times Mercury was ejected")
plt.xticks(abin)
plt.savefig("min_dist_merc.png")
plt.close()
