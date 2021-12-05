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
        self.narray = np.array(a)
        # Transpose numpy array
        self.narray = self.narray.transpose()
        
        # Get most significant bit and least count
        cnt = []
        gamma = ""
        epsilon = ""
        for row in self.narray:
            cnt = Counter(row)
            if cnt[0] > cnt[1]:
                gamma += "0"
                epsilon += "1"
            else:
                gamma += "1"
                epsilon += "0"
                
        # Calculate power consumption
        return (int(gamma, 2) * int(epsilon, 2))

    def part2(self):
        # oxyarray_tpose is the transpose of the transpose so original dataset format
        # co2array_tpose is the transpose of the transpose so original dataset format
        self.oxyarray_tpose = self.narray.transpose()
        self.oxyarray = self.narray.copy()
        self.co2array = self.narray.copy()
        self.co2array_tpose = self.narray.copy().transpose()
        t_count = 0
        while len(self.oxyarray_tpose) != 1 or len(self.co2array_tpose) != 1:
            cnt = Counter(self.oxyarray[t_count])
            if cnt[0] > cnt[1]:
                most_sig = 0
                least_sig = 1
            elif cnt[1] > cnt[0] or cnt[1] == cnt[0]:
                most_sig = 1
                least_sig = 0
            remove = []
            if len(self.oxyarray_tpose) != 1:
                for row_array in self.oxyarray_tpose:
                    if row_array[t_count] == most_sig:
                        remove.append(False)
                    else:
                        remove.append(True)
                self.oxyarray_tpose = np.delete(self.oxyarray_tpose, remove, 0)
                self.oxyarray = self.oxyarray_tpose.transpose()
            remove = []
            if len(self.co2array_tpose) != 1:
                for row_array in self.co2array_tpose:
                    if row_array[t_count] == least_sig:
                        remove.append(False)
                    else:
                        remove.append(True)
                self.co2array_tpose = np.delete(self.co2array_tpose, remove, 0)
                self.co2array = self.co2array_tpose.transpose()
            t_count += 1
        oxynum = int(''.join(str(e) for e in self.oxyarray_tpose[0].tolist()), 2)
        co2num = int(''.join(str(e) for e in self.co2array_tpose[0].tolist()), 2)
        return (oxynum * co2num)
                
            
            

# For testing
if __name__ == "__main__":
    
    d3 = Day3('day3.txt')
    
    print(d3.part1())
    print(d3.part2())