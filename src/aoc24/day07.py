async def day07():

    with open("data/day07.txt") as infile:
        lines = [line.strip().split(": ") for line in infile]

    from itertools import chain, combinations_with_replacement, permutations

    part1 = 0
    operators = ["+","*"]
    for line_i,line in enumerate(lines):
        solution, values = int(line[0]), line[1].split(" ")
        print(solution, values)
        num_ops = len(values) - 1
        for combo in combinations_with_replacement(operators,len(values)-1):
            for ops in set(permutations(combo,len(values)-1)):
                print("\t", ops)
                result = values[0]
                for i,op in enumerate(ops):
                    result = eval(f"{result} {op} {values[i+1]}")
                    if result > solution: break
                if result == solution:
                    part1 += result
                    break

    print(f"Day 07 | Part 1: {part1}      | {'Correct' if part1 == 5531 else 'Wrong'}")
            