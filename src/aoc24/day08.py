from collections import OrderedDict
import copy

async def day08():

    with open("data/day08.txt") as infile:
        lines = [[c for c in l.strip()] for l in infile]
    w,h = len(lines[0]), len(lines)

    debug_lines = copy.deepcopy(lines)

    # Locate all antennas
    # Calculate pairwise distances of each set and place their antinodes

    part1 = 0
    antennas = OrderedDict()
    coords = OrderedDict()
    for y1,line in enumerate(lines):
        for x1,c in enumerate(line):
            if c == ".": continue
            if c not in antennas:
                antennas[c] = [(x1, y1)]
                continue
            antennas[c].append((x1,y1))

            for x2,y2 in antennas[c]:
                if x1 == x2 and y1 == y2: continue
                a1 = x1 + (x1 - x2), y1 + (y1 - y2)
                a2 = x2 - (x1 - x2), y2 - (y1 - y2)
                #print(f"{c}: ({x1}, {y1}) --> ({x2}, {y2}), a1={a1}, a2={a2}")

                for ax,ay in [a1, a2]:
                    if ax >= 0 and ax < w and ay >= 0 and ay < h:
                        coords[(ax, ay)] = c
                        debug_lines[ay][ax] = "#"
                        #print("\t", a1)

    for line in lines:
        print("".join(line))
    print("-"* 80)
    for line in debug_lines:
        print("".join(line))

    part1 = len(coords)

    print(f"Day 08 | Part 1: {part1}      | {'Correct' if part1 == 1 else 'Wrong'}")
    part2 = 0
    print(f"       | Part 2: {part2}      | {'Correct' if part2 == 1 else 'Wrong'}")
       