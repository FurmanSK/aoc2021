import pytest
import day1


def test_day1():
    # read in file
    f = open('sample.txt', 'r')

    sonar_data = f.read().splitlines()
    
    assert day1.part1(sonar_data) == 7

def test_day1_part2():
    # read in file
    f = open('sample.txt', 'r')

    sonar_data = f.read().splitlines()
    
    assert day1.part2(sonar_data) == 5