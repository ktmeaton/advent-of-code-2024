async def day09():

    with open("data/day09_test.txt") as infile:
        lines = [line.strip().split(": ") for line in infile]

    part1 = 0
    print(f"Day 09 | Part 1: {part1}      | {'Correct' if part1 == 1 else 'Wrong'}")
    part2 = 0
    print(f"       | Part 2: {part2}      | {'Correct' if part2 == 1 else 'Wrong'}")
       