#!/bin/python3
import argparse

from day1.day1 import Day1
from day2.day2 import Day2
from day3.day3 import Day3


if __name__ == "__main__":
    ver = "2021 Advent Of Code solver ver 0.2 by Wes Forman"

    parser = argparse.ArgumentParser(description="Advent of Code 2021 Solver")
    parser.add_argument('-d', '--day', type=int, help="Which day to solve.")
    parser.add_argument('-a', '--all')
    parser.add_argument('-v', '--version', action="version", version=ver, help="Version of solver")
    
    args = parser.parse_args()
    
    if args.day:
        print("Solution to Day %d" % args.day)
        if args.day == 1:
            d1 = Day1('day1/input.txt')
            print(d1.part1())
            print(d1.part2())
        if args.day == 2:
            d2 = Day2('day2/input.txt')
            print(d2.part1())
            print(d2.part2())
        if args.day == 3:
            d3 = Day3('day3/day3.txt')
            print(d3.part1())
            print(d3.part2())