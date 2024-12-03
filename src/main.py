#!/usr/bin/env python

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
    print(f"Day 01 | Part 1: {result}  | {'Correct' if result == 1223326 else 'Wrong'}")
    result = sum([c1*col2.count(c1) for c1 in col1])
    print(f"       | Part 2: {result} | {'Correct' if result == 21070419 else 'Wrong'}")


def day02():
    """Day 02: Detecting bad levels in the fusion plant."""

    def is_safe(levels):
        sorted_levels = sorted(levels)
        diff = [abs(levels[i+1] - levels[i]) for i in range(0, len(levels)-1)]
        return (
            (levels == sorted_levels or levels == list(reversed(sorted_levels)))
            and (min(diff) >= 1 and max(diff) <= 3)
        )

    with open("data/day02.txt") as infile:
        lines = infile.readlines()
    
    result = 0
    unsafe = []

    for line in lines:
        levels = [int(l) for l in line.strip().split(" ")]
        safe = is_safe(levels)
        if not safe: unsafe.append(levels)
        result += 1 if safe else 0
    print(f"Day 02 | Part 1: {result}      | {'Correct' if result == 524 else 'Wrong'}")

    for levels in unsafe:
        for i in range(0, len(levels)):
            leave_one_out = levels[:i] + levels[i+1:]
            safe = is_safe(leave_one_out)
            if safe:
                result += 1
                break
    print(f"       | Part 2: {result}      | {'Correct' if result == 569 else 'Wrong'}")
    

def day03():
    import re

    with open("data/day03_test.txt") as infile:
        line = infile.read()

    def mul(x,y): return x * y
    result = 0
    regex = "mul\([\s0-9]+,[\s0-9]+\)"
    for match in re.findall( "mul\([\s0-9]+,[\s0-9]+\)", line):
        result += eval(match)
    print(result)

    prev = 0
    print(line)
    for match in re.finditer(regex, line):
        #result += eval(match)
        start, end = match.start(0), match.end(0)
        match = line[start:end]
        upstream = line[prev:start]
        print(match, start, end, upstream)
        prev = end
    print(result)


if __name__ == "__main__":
    #day01()
    #day02()
    day03()