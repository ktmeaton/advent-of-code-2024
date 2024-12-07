#!/usr/bin/env python3

def day01():
    """Day 01: Comparing two lists of historical locations."""

    with open("data/day01.txt") as infile:
        lines = infile.readlines()

    col1, col2 = [], []
    for line in lines:
        c1, c2 = [int(l.strip()) for l in line.split(" ") if l != ""]
        col1.append(c1)
        col2.append(c2)

    result = sum([abs(c1 - c2) for c1, c2 in zip(sorted(col1), sorted(col2))])
    print(f"Day 01 | Part 1: {result}   | {'Correct' if result == 1223326 else 'Wrong'}")
    result = sum([c1*col2.count(c1) for c1 in col1])
    print(f"       | Part 2: {result}  | {'Correct' if result == 21070419 else 'Wrong'}")