'''
Peter Duggins
June 3, 2019
ECE 750
Assignment 3
'''

import numpy as np
import matplotlib.pyplot as plt


def five(p, neighborhood, steps=10, length=100, seed=0):
	# initialization
	print("p=%s, neighborhood=%s" %(p, neighborhood))
	world_old = np.zeros((length, ))
	world_new = np.zeros((length, ))
	rng = np.random.RandomState(seed=seed)
	for idx in range(10):
		world_old[idx] = rng.randint(p)
	world_init = world_old
	# update loop
	for i in range(steps):
		for idx in range(world_old.shape[0]):
			if neighborhood == 'left':   # new state = left neighbor modulo p
				world_new[idx] = np.mod(world_old[idx-1], p)
			if neighborhood == 'radius':  # new state = sum of {left, center, right} modulo p
				left = idx-1
				center = idx
				right = np.mod(idx+1, length)  # impose toroidal boundary conditions
				world_new[idx] = np.mod(np.sum(
					[world_old[left], world_old[center], world_old[right]]), p)
		world_old = np.array(world_new)  # update world state
	fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
	ax1.imshow(np.expand_dims(world_init, axis=0))
	ax2.imshow(np.expand_dims(world_old, axis=0))
	ax1.set(title='world_init')
	ax2.set(title='world_final')
	plt.show()


def six(p, neighborhood, steps=10, length=30, seed=0):
	# initialization
	print("p=%s, neighborhood=%s" %(p, neighborhood))
	world_old = np.zeros((length, length))
	world_new = np.zeros((length, length))
	rng = np.random.RandomState(seed=seed)
	for x in range(3):
		for y in range(3):
			world_old[x, y] = rng.randint(p)
	world_init = world_old
	# update loop
	for i in range(steps):
		for x in range(world_old.shape[0]):
			for y in range(world_old.shape[1]):
				if neighborhood == 'left-top-center':   # new state = sum of {left, center, top} modulo p
					left = world_old[x-1, y]
					center = world_old[x, y]
					top = world_old[x, y-1]
					world_new[x, y] = np.mod(np.sum([left, center, top]), p)
				if neighborhood == 'von-Neumann':  # new state = sum of {left, center, right, top, bottom} modulo p
					left = world_old[x-1, y]
					center = world_old[x, y]
					top = world_old[x, y-1]
					# impose toroidal boundary conditions
					right = world_old[np.mod(x+1, world_old.shape[0]), y]
					bottom = world_old[x, np.mod(y+1, world_old.shape[0])]
					world_new[x, y] = np.mod(np.sum([left, center, top, right, bottom]), p)
		world_old = np.array(world_new)  # update world state
	fig, (ax1, ax2) = plt.subplots(1, 2)
	ax1.imshow(world_init)
	ax2.imshow(world_old)
	ax1.set(title='world_init')
	ax2.set(title='world_final')
	plt.show()

if __name__ == "__main__":
	five(p=2, neighborhood='left')
	five(p=5, neighborhood='left')
	five(p=11, neighborhood='left')

	five(p=2, neighborhood='radius')
	five(p=5, neighborhood='radius')
	five(p=11, neighborhood='radius')

	print('lools like the radius 1 neighborhood breaks replication')

	six(p=5, seed=1, neighborhood='left-top-center')

	six(p=5, seed=1, neighborhood='von-Neumann')

	print('both 2D neighborhoods produce a copy and a mutated copy of the initial state')

