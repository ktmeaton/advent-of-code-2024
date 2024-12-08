async def day07():

    with open("data/day07.txt") as infile:
        lines = [line.strip().split(": ") for line in infile]

    from itertools import chain, combinations

    def powerset(ops):
        return chain.from_iterable(combinations(ops, r) for r in range(len(ops)))

    part1 = 0
    ops = "*+"
    for line_i,line in enumerate(lines):
        print(line_i)
        solution, values = int(line[0]), [int(l) for l in line[1].split(" ")]
        num_ops = len(values) - 1
        combos = set()
        for p in powerset("*+" * num_ops):
            if len(p) != num_ops: continue
            combos.add(p)
        result = values[0]
        for c in combos:
            result = values[0]
            for i,op in enumerate(c):
                result = eval(f"{result} {op} {values[i+1]}")
                if result > solution: break
            if result == solution:
                part1 += result
                break
        # for c in combos:
        #     e = equation.format(*c)
        #     r = eval(e)
        #     print(solution, "|", r, "=", e)
        #     # if r == solution:
        #     #     print(solution, e)
        #     #     part1 += solution
        #     #     break

    print(f"Day 07 | Part 1: {part1}      | {'Correct' if part1 == 5531 else 'Wrong'}")
            