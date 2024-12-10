async def day10():

    with open("data/day10.txt") as infile:
        lines = [[int(c) if c != "." else "." for c in line.strip()] for line in infile]

    w,h = len(lines[0]), len(lines)

    def follow_paths(c, x, y, w, h, lines, final:int=9):
        paths = []
        if c == final:
            return [(c,x,y)]
        elif c == ".":
            return []
        else:
            new_paths = []
            if y < (h-1) and lines[y+1][x] == c+1:
                for p in follow_paths(c+1, x, y+1, w, h, lines):
                    new_paths.append(p)
            if x < (w-1) and lines[y][x+1] == c+1:
                for p in follow_paths(c+1, x+1, y, w, h, lines):
                    new_paths.append(p)
            if x > 0 and lines[y][x-1] == c+1:
                for p in follow_paths(c+1, x-1, y, w, h, lines):
                    new_paths.append(p)
            if y > 0 and lines[y-1][x] == c+1:
                for p in follow_paths(c+1, x, y-1, w, h, lines):
                    new_paths.append(p)
            for p in new_paths:
                p = [(c, x, y)] + ([p] if type(p) != list else p)
                paths.append(p)
        return paths

    part1 = 0
    part2 = 0

    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c != 0: continue
            paths = follow_paths(c, x, y, w, h, lines)
            part2 += len(paths)
            unique_ends = set(p[-1] for p in paths)
            part1 += len(unique_ends)

    print(f"Day 10 | Part 1: {part1}      | {'Correct' if part1 == 1 else 'Wrong'}")
    print(f"       | Part 2: {part2}      | {'Correct' if part2 == 1 else 'Wrong'}")
       