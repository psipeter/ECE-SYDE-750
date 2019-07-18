'''
Peter Duggins
July 22, 2018
ECE 750
Assignment 8: Growth and Morphogenesis II: computational morphogenesis, positional information, and symmetry
'''

import numpy as np
import matplotlib.pyplot as plt
import copy

def solution1():
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
	plt.show()

def solution2():
	# solution 2: 2D CA grid with local reproduction rules and discrete X diffusion through cells
	class Cell():
		def __init__(self, x, y, X):
			self.x = x
			self.y = y
			self.X = X

	def reproduce(cell, cells, grid, rng):
		# produce a new cell to the right (50%) or down (50%) if either space is empty
		if cell.x+1 >= grid.shape[0] or cell.y+1 >= grid.shape[1]:
			return grid, cells
		if rng.uniform(0, 1) < 0.5 and grid[cell.x+1, cell.y] == 0:
			offspring = Cell(cell.x+1, cell.y, cell.X-1.0/grid.shape[0])
			cells.append(offspring)
			grid[cell.x+1, cell.y] = [offspring]
		elif grid[cell.x, cell.y+1] == 0:
			offspring = Cell(cell.x, cell.y+1, cell.X)
			cells.append(offspring)
			grid[cell.x, cell.y+1] = [offspring]
		return grid, cells

	xmax = 30
	ymax = 20
	grid = np.zeros((xmax, ymax), dtype=list)
	rng = np.random.RandomState(seed=0)
	cells = [Cell(0, 0, 1.0)]
	t_final = 60
	for t in range(t_final):
		print("t=%s, n_cells=%s" %(t, len(cells)))
		for cell in copy.deepcopy(cells):
			grid, cells = reproduce(cell, cells, grid, rng)
	rng.shuffle(cells)
	fig, ax = plt.subplots()
	for cell in cells:
		color = 'w'
		if 0.0 <= cell.X < 0.33:
			color = 'r'
		elif 0.33 < cell.X < 0.66:
			color = 'w'
		elif 0.66 < cell.X <= 1.0:
			color = 'b'
		ax.scatter(cell.x, cell.y, c=color, marker='s', s=100)
	ax.set(xlim=((-1, xmax)), ylim=((-1, ymax)))
	plt.show()

# solution1()
solution2()