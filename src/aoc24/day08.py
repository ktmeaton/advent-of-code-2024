from collections import OrderedDict
import copy

async def day08():

    with open("data/day08.txt") as infile:
        lines = [[c for c in l.strip()] for l in infile]
    w,h = len(lines[0]), len(lines)

    debug_lines = copy.deepcopy(lines)

    # Locate all antennas
    # Calculate pairwise distances of each set and place their antinodes

    part1 = set()
    part2 = set()
    antennas = OrderedDict()
    for y1,line in enumerate(lines):
        for x1,c in enumerate(line):
            if c == ".": continue
            if c not in antennas:
                antennas[c] = [(x1, y1)]
                continue
            antennas[c].append((x1,y1))
            for x2,y2 in antennas[c]:
                if x1 == x2 and y1 == y2: continue
                for name in ["a1", "a2"]:
                    vx, vy = (x1 - x2, y1 - y2) if name == "a1" else (x2 - x1, y2 - y1)
                    ax, ay = (x1 + vx, y1 + vy) if name == "a1" else (x2 + vx, y2 + vy)
                    seen_part1 = False
                    #print("-" * 80)
                    #print(f"x: {ax}, y: {ay}, vx: {vx}, vy: {vy}")
                    while ax >= 0 and ax < w and ay >= 0 and ay < h:
                        debug_lines[ay][ax] = "#"
                        if not seen_part1:
                            part1.add((ax, ay))
                            seen_part1 = True
                        part2.add((ax, ay))
                        ax, ay = (ax + vx, ay + vy)

    # for line in lines:
    #     print("".join(line))
    # print("-"* 80)
    # for line in debug_lines:
    #     print("".join(line))

    part1 = len(part1)
    print(f"Day 08 | Part 1: {part1}      | {'Correct' if part1 == 1 else 'Wrong'}")
    for coords in antennas.values():
        if len(coords) <= 1: continue
        new = set(c for c in coords if c not in part2)
        part2.update(new)
        #new = [coord for coord in coords if coord not in part2]
        #part2 += len(new)
    part2 = len(part2)
    print(f"       | Part 2: {part2}      | {'Correct' if part2 == 1 else 'Wrong'}")
       