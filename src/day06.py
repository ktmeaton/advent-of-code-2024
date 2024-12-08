#!/usr/bin/env python3

def step(x,y,d):
    x += 1 if d == "right" else -1 if d == "left" else 0
    y += 1 if d == "down"  else -1 if d == "up"   else 0
    return(x, y) 

async def day06():
    """Predicting a guard's patrol pattern."""

    with open("data/day06.txt") as infile:
        lines = [line.strip() for line in infile]

    x1, y1, d = 0, 0, "up"
    w, h = len(lines[0]), len(lines)
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c == "^":
                x1, y1 = x, y
                break
    x2, y2 = x1, y1

    steps = 0
    coords = set()
    coords.add((x1,y1))

    while True:
        x2, y2 = step(x1, y1, d)
        if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
            break
        c = lines[y2][x2]
        while c == "#":
            d = "right" if d == "up" else "down" if d == "right" else "left" if d == "down" else "up"
            x2, y2 = step(x1, y1, d)
            c = lines[y2][x2]

        x1, y1 = x2, y2
        coords.add((x1, y1))
        steps += 1

    part1 = len(coords)    
    print(f"Day 06 | Part 1: {part1}      | {'Correct' if part1 == 5531 else 'Wrong'}")
    part2  = 0
    # Loops!
    # We can only place one obstacle, so we limit it to coordinates that the guard traverses
    # Which is still 5000+ coords, so brute forcing isn't my #1 strategy
    # Or could we?

    print(f"       | Part 2: {part2}      | {'Correct' if part2 == 6142 else 'Wrong'}")

if __name__ == "__main__":
    day06()