# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal
import rle

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int64)
        self.neighborhood = np.ones((3,3), np.int64) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        # get weighted sum of neighbors
        # PART A & E CODE HERE

        if self.fastMode is True:
            summed_neighbors = signal.convolve2d(self.grid, self.neighborhood, mode='same', boundary='fill')
        else:
            weights = np.zeros_like(self.grid)
            for i in range(weights.shape[0]):
                for j in range(weights.shape[1]):
                    total = np.sum(self.grid[i - 1:i + 2, j - 1:j + 2]) - self.grid[i, j]
                    weights[i, j] = total
            summed_neighbors = weights

            # implement the GoL rules by thresholding the weights
        new_grid = np.where((self.grid == self.aliveValue) & ((summed_neighbors < 2) | (summed_neighbors > 3)),
                            self.deadValue, self.grid)

        new_grid = np.where((self.grid == self.aliveValue) & ((summed_neighbors == 2) | (summed_neighbors == 3)),
                            self.aliveValue, new_grid)

        new_grid = np.where((self.grid == self.aliveValue) & (summed_neighbors > 3), self.deadValue, new_grid)

        new_grid = np.where((self.grid == self.deadValue) & (summed_neighbors == 3),
                            self.aliveValue, new_grid)

        # update the grid
        self.grid = new_grid
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue  # remove a duplicate line
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        
    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human-readable pattern without comments
        '''
        # Split the txtString into lines
        lines = txtString.splitlines()

        # Create a new grid to store the updated states
        new_grid = np.zeros((self.grid.shape[0], self.grid.shape[1]), np.int64)

        # Iterate over each line and insert the pattern into the grid
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == 'O':  # Alive cell
                    new_grid[y + pad, x + pad] = self.aliveValue
                elif char == '.':  # Dead cell
                    new_grid[y + pad, x + pad] = self.deadValue

        # Update the grid with the new pattern
        self.grid = new_grid

    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
        # parses the RLE string and creates a 2D array representation of the pattern
        parser = rle.RunLengthEncodedParser(rleString)
        # contains this 2D array representation of the pattern
        pattern = parser.pattern_2d_array

        for y in range(len(pattern)):
            for x in range(len(pattern[0])):
                if pattern[y][x] == 'o':
                    self.grid[y + pad, x + pad] = self.aliveValue
        