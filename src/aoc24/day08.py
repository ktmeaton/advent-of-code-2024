async def day08():

    with open("data/day08.txt") as infile:
        lines = [[c for c in l.strip()] for l in infile]

    w,h = len(lines[0]), len(lines)
    part1 = set()
    part2 = set()
    antennas = {}

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
                    while ax >= 0 and ax < w and ay >= 0 and ay < h:
                        if not seen_part1:
                            part1.add((ax, ay))
                            seen_part1 = True
                        part2.add((ax, ay))
                        ax, ay = (ax + vx, ay + vy)

    part1 = len(part1)
    print(f"Day 08 | Part 1: {part1}      | {'Correct' if part1 == 320 else 'Wrong'}")

    for coords in [c for c in antennas.values() if len(c) > 1]:
        part2.update(set(c for c in coords if c not in part2))
    part2 = len(part2)
    print(f"       | Part 2: {part2}     | {'Correct' if part2 == 1157 else 'Wrong'}")
       