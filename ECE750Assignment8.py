'''
Peter Duggins
July 22, 2018
ECE 750
Assignment 8: Growth and Morphogenesis II: computational morphogenesis, positional information, and symmetry
'''

import numpy as np
import matplotlib.pyplot as plt

# solution 1: 2D CA grid on top of continuous X concentration
xmax = 30
ymax = 20
grid = np.zeros((xmax, ymax), dtype=str)
# varies from 1 on left (x=0) to 0 on the right (x=grid[-1])
Fx = lambda x: 1.0 - 1.0*x/grid.shape[0]
for x in range(xmax):
	for y in range(ymax):
		# get concentration value from underlying continuous function
		X = Fx(x)
		# discretize into red, white, or blue stripe
		color = 'w'
		if 0.0 <= X < 0.33:
			color = 'r'
		elif 0.33 < X < 0.66:
			color = 'w'
		elif 0.66 < X <= 1.0:
			color = 'b'
		# print(color)
		# update CA grid (cell positioned at x, y)
		grid[x, y] = color

fig, ax = plt.subplots()
for x in range(xmax):
	for y in range(ymax):
		ax.scatter(x, y, c=grid[x, y], marker='s', s=100)
# ax.set(xlim=((0, xmax)), ylim=((0, ymax)))
plt.show()