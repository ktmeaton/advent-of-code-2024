#!/usr/bin/env python3

async def day01():
    """Day 01: Comparing two lists of historical locations."""

    with open("data/day01.txt") as infile:
        lines = infile.readlines()

    col1, col2 = [], []
    for line in lines:
        c1, c2 = [int(l.strip()) for l in line.split(" ") if l != ""]
        col1.append(c1)
        col2.append(c2)

    part1 = sum([abs(c1 - c2) for c1, c2 in zip(sorted(col1), sorted(col2))])
    print(f"Day 01 | Part 1: {part1}   | {'Correct' if part1 == 1223326 else 'Wrong'}")
    part2 = sum([c1*col2.count(c1) for c1 in col1])
    print(f"       | Part 2: {part2}  | {'Correct' if part2 == 21070419 else 'Wrong'}")

    return(part1, part2)