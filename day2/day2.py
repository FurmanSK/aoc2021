#!/bin/python3

class Day2:
    
    def __init__(self, file):
        self.data = open(file, 'r').read().splitlines()
        self.coord1 = [0, 0]
        self.coord2 = [0, 0, 0]
        
    def part1(self):
        
        for x in range(len(self.data)):
            line = self.data[x].split()
            if line[0] == 'forward':
                self.coord1[0] += int(line[1])
            elif line[0] == 'down':
                self.coord1[1] += int(line[1])
            elif line[0] == 'up':
                self.coord1[1] -= int(line[1])
        
        return self.coord1[0] * self.coord1[1]
    
    def part2(self):
        for x in range(len(self.data)):
            line = self.data[x].split()
            if line[0] == 'forward':
                self.coord2[0] += int(line[1])
                self.coord2[1] += int(line[1]) * self.coord2[2]
            elif line[0] == 'down':
                self.coord2[2] += int(line[1])
            elif line[0] == 'up':
                self.coord2[2] -= int(line[1])
        
        return self.coord2[0] * self.coord2[1]
    

if __name__ == "__main__":
    
    d2 = Day2('input.txt')
    
    print(d2.part1())
    print(d2.part2())