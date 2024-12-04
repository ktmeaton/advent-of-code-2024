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
    print(f"Day 01 | Part 1: {result}   | {'Correct' if result == 1223326 else 'Wrong'}")
    result = sum([c1*col2.count(c1) for c1 in col1])
    print(f"       | Part 2: {result}  | {'Correct' if result == 21070419 else 'Wrong'}")


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
    print(f"Day 02 | Part 1: {result}       | {'Correct' if result == 524 else 'Wrong'}")

    for levels in unsafe:
        for i in range(0, len(levels)):
            leave_one_out = levels[:i] + levels[i+1:]
            safe = is_safe(leave_one_out)
            if safe:
                result += 1
                break
    print(f"       | Part 2: {result}       | {'Correct' if result == 569 else 'Wrong'}")
    

def day03():
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


def day04():
    """The XMAX word search."""

    def search(buffer, pattern, ignore="."):
        "Search for a 2D pattern in a 2D buffer."
        coords = []

        bw, bh = len(buffer[0]), len(buffer)
        pw, ph = len(pattern[0]), len(pattern)
        ignore_coords = []
        for y in range(0, ph):
            for x in range(0, pw):
                c = pattern[y][x]
                if c == ignore:
                    ignore_coords.append((x,y))

        for y in range(0, bh):
            for x in range(0, bw):
                if x+pw > bw or y+ph > bh: continue
                chars = [l[x:x+pw] for l in buffer[y:y+ph]]
                split = [[c for c in line] for line in chars]
                for (ix,iy) in ignore_coords: split[iy][ix] = "."
                chars = ["".join(l) for  l in split]
                if chars == pattern:
                    coords.append((x,y)) 
        return coords

    def word_search_patterns(text):
        """Create all patterns of a text in a word search"""
        return [
            [text],
            [text[::-1]],
            [c for c in text],
            [c for c in text[::-1]],
            [f"{'.'*i}{c}{'.'*(len(text)-1-i)}" for i,c in enumerate(text)],
            [f"{'.'*i}{c}{'.'*(len(text)-1-i)}" for i,c in enumerate(text[::-1])],
            [f"{'.'*(len(text)-1-i)}{c}{'.'*i}" for i,c in enumerate(text)],
            [f"{'.'*(len(text)-1-i)}{c}{'.'*i}" for i,c in enumerate(text[::-1])],
        ]

    with open("data/day04.txt") as infile:
        lines = [l.strip() for l in infile.readlines()]

    # Part 1
    result = 0
    for pattern in word_search_patterns("XMAS"):
        matches = search(lines, pattern)
        result += len(matches)
    print(f"Day 04 | Part 1: {result}      | {'Correct' if result == 2599 else 'Wrong'}")

    # Part 2
    patterns = [["M.S", ".A.", "M.S"], ["S.M", ".A.", "S.M"], ["M.M", ".A.", "S.S"], ["S.S", ".A.", "M.M"]]
    result = 0
    for pattern in patterns:
        matches = search(lines, pattern)
        result += len(matches)
    print(f"       | Part 2: {result}      | {'Correct' if result == 1948 else 'Wrong'}")

if __name__ == "__main__":
    day01()
    day02()
    day03()
    day04()