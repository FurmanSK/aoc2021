import pytest
from day1.day1 import Day1

d1 = Day1('day1/sample.txt')

def test_day1_part1():    
    assert d1.part1() == 7

def test_day1_part2():
    assert d1.part2() == 5