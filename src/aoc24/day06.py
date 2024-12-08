#!/usr/bin/env python3

def step_forward(x,y,d):
    x += 1 if d == "right" else -1 if d == "left" else 0
    y += 1 if d == "down"  else -1 if d == "up"   else 0
    return(x, y)

def step_backward(x,y,d):
    x += -1 if d == "right" else 1 if d == "left" else 0
    y += -1 if d == "down"  else 1 if d == "up"   else 0
    return(x, y)

def change_direction(d):
    return "right" if d == "up" else "down" if d == "right" else "left" if d == "down" else "up"

async def path_coords(x,y,d,grid):
    w,h = len(grid[0]), len(grid)
    if d == "right":
        coords = [(x1,y) for x1 in range(x+1,w)]
    elif d == "left":
        coords = [(x1,y) for x1 in list(reversed(range(0,x)))]
    elif d == "up":
        coords = [(x,y1) for y1 in list(reversed(range(0,y)))]
    elif d == "down":
        coords = [(x,y1) for y1 in range(y+1,h)]

    path = "".join([grid[y][x] for x,y in coords])
    return(path, coords)

async def day06():
    """Predicting a guard's patrol pattern."""

    from collections import OrderedDict
    import copy

    with open("data/day06.txt") as infile:
        lines = [line.strip() for line in infile]

    # Locate the guard's starting position
    w, h = len(lines[0]), len(lines)
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c == "^":
                gx, gy, gd = x, y, "up"
                break

    # Find how many unique coordinates the guard enters
    # keeping track of the direction when they first enter
    unique_coords = {(gx, gy): gd}
    x1, y1, d, x2, y2 = gx, gy, gd, gx, gy

    while x2 >= 0 and x2 < (w-1) and y2 >= 0 and y2 < (h-1):
        x2, y2 = step_forward(x1, y1, d)
        while lines[y2][x2] == "#":
            d = change_direction(d)
            x2, y2 = step_forward(x1, y1, d)
        x1, y1 = x2, y2
        if (x1,y1) not in unique_coords:
            unique_coords[(x1,y1)] = d

    part1 = len(unique_coords)    
    print(f"Day 06 | Part 1: {part1}      | {'Correct' if part1 == 5531 else 'Wrong'}")

    part2  = 0

    lines = [[c for c in line] for line in lines]
    for obxy_i,obxy in enumerate(unique_coords):
        # Skip the guard's starting position
        if obxy == (gx, gy): continue
        obx, oby, d = obxy[0], obxy[1], unique_coords[obxy]
        lines[oby][obx] = "#"

        # Figure out where the guard was before hiting our new obstacle
        x,y = step_backward(obx, oby, d)
        d = change_direction(d)

        # Check if the next travel path contains an obstacle
        path, coords = await path_coords(x,y,d,lines)
        if "#" not in path: 
            lines[oby][obx] = "."
            continue

        # If it does, this is a loop candidate
        seen = [[(x,y)]]
        while "#" in path:
            # Tidy up latest coords
            i = [i for i,c in enumerate(path) if c == "#"][0] - 1
            coords = coords[0:i+1]
            if coords in seen:
                part2 += 1
                break
            elif coords != []:
                seen.append(coords)

            # Get the next path to test
            if len(coords) > 0:
                x, y = coords[-1][0], coords[-1][1]
            d = change_direction(d)
            path, coords = await path_coords(x,y,d,lines)

        # Reset the obstacle
        lines[oby][obx] = "."


    print(f"       | Part 2: {part2}      | {'Correct' if part2 == 2165 else 'Wrong'}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(day06())
