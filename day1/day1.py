#!/bin/python3

class Day1():
    
    def __init__(self, file):
        f = open(file, 'r')
        self.sonar_data = f.read().splitlines()
        f.close()
    
    def part1(self):       
        # run through checking for increase or decrease

        new_num = 0
        prev_num = 0

        increase_count = 0

        for i in range(len(self.sonar_data)):
            if i == 0:
                prev_num = int(self.sonar_data[i])
            else:
                new_num = int(self.sonar_data[i])
                diff = new_num - prev_num
                if diff > 0:
                    increase_count += 1
                prev_num = new_num   
        return increase_count

    def part2(self):
        prev_win = [0, 1, 2]
        increase_count = 0
        for i in range(len(self.sonar_data)):
            try:
                prev_sum = int(self.sonar_data[prev_win[0]]) + int(self.sonar_data[prev_win[1]]) + int(self.sonar_data[prev_win[2]])
                next_sum = int(self.sonar_data[prev_win[0]+1]) + int(self.sonar_data[prev_win[1]+1]) + int(self.sonar_data[prev_win[2]+1])
                
                if next_sum> prev_sum:
                    increase_count += 1
                    
                prev_win[0] += 1
                prev_win[1] += 1
                prev_win[2] += 1
            except:
                return increase_count
                
            

if __name__ == "__main__":

    d1 = Day1('input.txt')

    print (d1.part1())
    print (d1.part2())