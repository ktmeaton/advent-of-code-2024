#!/usr/bin/env python3

async def search(b, p, ignore="."):
    "Search a 2D buffer (b) for a 2D pattern (p)."
    coords, ignore_coords = [], []
    pw, ph, bw, bh = len(p[0]), len(p), len(b[0]), len(b)
    # Search for coordinates to ignore
    for y,line in enumerate(p):
        for x,c in enumerate(line):
            if line[x] == ignore:
                ignore_coords.append((x,y))
    # Search for pattern in buffer
    for y,line in enumerate(b):
        if y+ph > bh: continue
        for x,c in enumerate(line):
            if x+pw > bw: continue
            chars = [l[x:x+pw] for l in b[y:y+ph]]
            split = [[c for c in line] for line in chars]
            for (ix,iy) in ignore_coords: split[iy][ix] = ignore
            if ["".join(l) for  l in split] == p: coords.append((x,y)) 
    return coords

async def word_search_patterns(text):
    """Create all patterns of a text in a word search"""
    return [
        [text], # Forward
        [text[::-1]], # Backward
        [c for c in text], # Down
        [c for c in text[::-1]], # Up
        [f"{'.'*i}{c}{'.'*(len(text)-1-i)}" for i,c in enumerate(text)], # Diagonal
        [f"{'.'*i}{c}{'.'*(len(text)-1-i)}" for i,c in enumerate(text[::-1])], # Diagonal
        [f"{'.'*(len(text)-1-i)}{c}{'.'*i}" for i,c in enumerate(text)], # Diagonal
        [f"{'.'*(len(text)-1-i)}{c}{'.'*i}" for i,c in enumerate(text[::-1])], # Diagonal
    ]

async def day04():
    """The XMAX word search."""

    with open("data/day04.txt") as infile:
        lines = [l.strip() for l in infile.readlines()]

    # Part 1
    result = 0
    for pattern in await word_search_patterns("XMAS"):
        matches = await search(lines, pattern)
        result += len(matches)
    print(f"Day 04 | Part 1: {result}      | {'Correct' if result == 2599 else 'Wrong'}")

    # Part 2
    patterns = [["M.S", ".A.", "M.S"], ["S.M", ".A.", "S.M"], ["M.M", ".A.", "S.S"], ["S.S", ".A.", "M.M"]]
    result = 0
    for pattern in patterns:
        matches = await search(lines, pattern)
        result += len(matches)
    print(f"       | Part 2: {result}      | {'Correct' if result == 1948 else 'Wrong'}")
