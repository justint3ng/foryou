# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def read_pattern(filepath):
    with open(filepath, "r") as file:
        return file.read()

filepath = '/Users/justin/Desktop/UQ/y2s1/comp2048/lab02/110p62.cells'

N = 64
padding = 5


# create the game of life object
life = conway.GameOfLife(N)
#life.insertBlinker((0,0))
#life.insertGlider((0,0))
#life.insertGliderGun((0,0))
pattern = read_pattern(filepath)
life.insertFromPlainText(pattern, padding)
cells = life.getStates()



# plot cells
fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life
    
    life.evolve()
    cellsUpdated = life.getStates()
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 200 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
