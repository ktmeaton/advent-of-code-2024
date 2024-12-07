#!/usr/bin/env python3

async def day03():
    import re

    with open("data/day03.txt") as infile:
        line = infile.read()

    def mul(x,y): return x * y
    result = 0
    regex1 = "mul\([\s0-9]+,[\s0-9]+\)"
    regex2 = "\)\((od|t'nod)"

    for match in re.findall(regex1, line):
        result += eval(match)
    print(f"Day 03 | Part 1: {result} | {'Correct' if result == 175615763 else 'Wrong'}")

    result = 0
    prev = 0
    enable = True
    for match in re.finditer(regex1, line):
        expr = match.group()
        start, end = match.start(0), match.end(0)
        upstream = line[prev:match.start()]
        matches = re.findall(regex2, upstream[::-1])
        if matches:
            if matches[0] == "t'nod":
                enable = False
            elif matches[0] == "od":
                enable = True
        result += eval(expr) if enable else 0
        prev = end
    print(f"       | Part 2: {result}  | {'Correct' if result == 74361272 else 'Wrong'}")
