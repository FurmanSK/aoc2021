#!/bin/python3

import numpy as np
from collections import Counter

class Day3():
    
    def __init__(self, file):
        self.data = open(file, 'r').read().splitlines()
        
    def part1(self):
        # Parse in and store broken chars in list
        a = []
        for x in self.data:
            tmp = [int(char) for char in x]
            a.append(tmp)
        
        # Convert to numpy array
        narray = np.array(a)
        # Transpose numpy array
        narray = narray.transpose()
        
        # Get most significant bit and least count
        cnt = []
        gamma = ""
        epsilon = ""
        for row in narray:
            cnt = Counter(row)
            if cnt[0] > cnt[1]:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"
                
        # Print and calculate power consumption
        # print("Gamma = ", int(gamma, 2))
        # print("epsilon = ", int(epsilon, 2))
        return (int(gamma, 2) * int(epsilon, 2))

# For testing
if __name__ == "__main__":
    
    d3 = Day3('sample.txt')
    
    d3.part1()