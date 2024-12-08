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

def path_coords(x,y,d,grid):
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

def day06():
    """Predicting a guard's patrol pattern."""

    from collections import OrderedDict
    import copy

    with open("data/day06.txt") as infile:
        lines = [line.strip() for line in infile]

    w, h = len(lines[0]), len(lines)
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c == "^":
                gx, gy, gd = x, y, "up"
                break

    unique_coords = {(gx, gy): gd}
    x1, y1, d = gx, gy, gd

    while True:
        x2, y2 = step_forward(x1, y1, d)
        if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h: break
        c = lines[y2][x2]
        while c == "#":
            d = change_direction(d)
            x2, y2 = step_forward(x1, y1, d)
            c = lines[y2][x2]
        x1, y1 = x2, y2
        if (x1,y1) not in unique_coords:
            unique_coords[(x1,y1)] = d

    part1 = len(unique_coords)    
    print(f"Day 06 | Part 1: {part1}      | {'Correct' if part1 == 5531 else 'Wrong'}")

    # tmp_lines = [[c for c in line] for line in lines]
    # for x,y in unique_coords:
    #     tmp_lines[y][x] = "X"
    # for line in tmp_lines:
    #     print("".join(line))
    # Loops!
    # We can only place one obstacle, so we limit it to coordinates that the guard traverses
    # Which is still 5000+ coords, so brute forcing isn't my #1 strategy
    # Or could we?
    part2  = 0

    testing = [(3,6), (6,7), (7, 7)]
    wrong = [ (8,5)]
    lines = [[c for c in line] for line in lines]
    for obxy_i,obxy in enumerate(unique_coords):
        print(obxy_i)
        # Skip the guard's starting position
        if obxy == (gx, gy): continue
        obx, oby, d = obxy[0], obxy[1], unique_coords[obxy]
        lines[oby][obx] = "#"
        debug_lines = copy.deepcopy(lines)
        # # For debugging
        # if obxy != testing[2]:
        #     lines[oby][obx] = "."
        #     continue
        # Figure out where the guard was before hiting our new obstacle
        x,y = step_backward(obx, oby, d)
        d = change_direction(d)

        # Check if the next travel path contains an obstacle
        path, coords = path_coords(x,y,d,lines)
        if "#" not in path: 
            lines[oby][obx] = "."
            continue

        # If it does, this is a loop candidate
        loop, seen = False, [[(x,y)]]
        while "#" in path:
            # Tidy up latest coords
            i = [i for i,c in enumerate(path) if c == "#"][0] - 1
            coords = coords[0:i+1]
            #print(f"x: {x}, y: {y}, d: {d}, path: {path}, coords: {coords}", coords in seen)

            if coords in seen:
                loop = True
                #print("LOOP FOUND")
                break
            elif coords != []:
                seen.append(coords)

            # Get the next path to test
            if len(coords) > 0:
                x, y = coords[-1][0], coords[-1][1]
            d = change_direction(d)
            path, coords = path_coords(x,y,d,lines)

            # # Debug
            # debug_seen = copy.deepcopy(seen)
            # if "#" not in path:
            #     debug_seen += [coords]
            # for d_i,d_cxy in enumerate(debug_seen):
            #     for d_cx,d_cy in d_cxy:
            #         debug_lines[d_cy][d_cx] = f"{d_i}"
            # debug_lines[gy][gx] = "^"
            # debug_lines[oby][obx] = "O"
            # print("-" * 20)
            # for line in debug_lines:
            #     print("".join(line))
            # print("-" * 20)

        #print("WHILE END")

        if loop:
            part2 += 1
            # # Debug
            # for i,coords in enumerate(seen):
            #     for cx,cy in coords:
            #         debug_lines[cy][cx] = f"{i}"
            # debug_lines[gy][gx] = "^"
            # debug_lines[oby][obx] = "O"
            # print("-" * 20)
            # for line in debug_lines:
            #     print("".join(line))
            # print("-" * 20)
            # break

        # Reset the obstacle
        lines[oby][obx] = "."
        debug_lines[oby][obx] = "."


    print(f"       | Part 2: {part2}      | {'Correct' if part1 == 5531 else 'Wrong'}")

    #for line in lines:
    #    print("".join(line))

if __name__ == "__main__":
    day06()
