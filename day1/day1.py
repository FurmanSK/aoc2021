#!/bin/python3
import sys

def part1(sonar_data):       
    # run through checking for increase or decrease

    new_num = 0
    prev_num = 0

    increase_count = 0

    for i in range(len(sonar_data)):
        if i == 0:
            prev_num = int(sonar_data[i])
        else:
            new_num = int(sonar_data[i])
            diff = new_num - prev_num
            if diff > 0:
                increase_count += 1
            prev_num = new_num   
    return increase_count

def part2(sonar_data):
    prev_win = [0, 1, 2]
    increase_count = 0
    for i in range(len(sonar_data)):
        try:
            prev_sum = int(sonar_data[prev_win[0]]) + int(sonar_data[prev_win[1]]) + int(sonar_data[prev_win[2]])
            next_sum = int(sonar_data[prev_win[0]+1]) + int(sonar_data[prev_win[1]+1]) + int(sonar_data[prev_win[2]+1])
            
            if next_sum> prev_sum:
                increase_count += 1
                
            prev_win[0] += 1
            prev_win[1] += 1
            prev_win[2] += 1
        except:
            print("end of array")
            return increase_count
            
            

if __name__ == "__main__":
    # read in file
    f = open('input.txt', 'r')

    sonar_data = f.read().splitlines()

    print (part1(sonar_data))
    print (part2(sonar_data))