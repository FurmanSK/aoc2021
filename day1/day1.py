#!/bin/python3

def day1(file):
    # read in file
    f = open(file, 'r')

    sonar_data = f.read().splitlines()

        
    # run through checking for increase or decrease

    new_num = 0
    prev_num = 0

    increase_count = 0
    decrease_count = 0
    diff = 0

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
