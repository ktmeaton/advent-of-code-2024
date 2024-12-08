#!/usr/bin/env python3

async def day02():
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
    