async def day07():

    with open("data/day07_test.txt") as infile:
        lines = [line.strip().split(": ") for line in infile]

    from itertools import chain, combinations_with_replacement, permutations

    part1 = 0
    for line_i,line in enumerate(lines):
        solution, values = int(line[0]), line[1].split(" ")
        num_parentheses = len(values) - 1
        equations = {}
        print(solution, values)
        while len(values) > 0:
            val = int(values.pop())
            data = [
                [{"op": "+", "val": val, "solution": solution - val}]
            ]
            if solution % val == 0:
                data.append([{"op": "*", "val": val, "solution": int(solution / val)}])
            new_equations = []
            for d in data:
                print("\t", d, len(equations) == 0)
                if len(equations) == 0: 
                    new_equations = data
                else:
                    for i,e in enumerate(equations):
                        print("\t", "-" * 60)
                        print("\t", i, e)
                        o, v, s = d[0].values()
                        #print("\t\t", f"val: {val}, solution: {tmp_solution}")
                        new_e = [{"op": o, "val": v, "solution": e[0]["solution"] - val}]
                        print("\t", i, new_e)
                        #new_equations.append(op + equations[i])

            equations = new_equations
            # for op in ops:
            #     if len(equations) == 0:
            #         equations[op] = 
            #     else:
            #         ...
            # if len(equations) == 0:
            #     equations = ops
            # else:
            #     new_equations = []
            #     for i in range(0,len(equations)):
            #         for op in ops:
            #             new_equations.append(op + equations[i])
            #     equations = new_equations
            #print(val, equations)
        # equations = [" ".join(["("] * num_parentheses + values + e) for e in equations]
        # solved = None
        # for e in equations:
        #     print(f"\t {eval(e)}={e}")
        #     if eval(e) == solution:
        #         part1 += 1
        #         solved = e
        #         break
        # print(f"\tsolved: {solved}")

    # operators = ["+","*"]
    # for line_i,line in enumerate(lines):
    #     solution, values = int(line[0]), line[1].split(" ")
    #     print(solution, values)
    #     num_ops = len(values) - 1
    #     for combo in combinations_with_replacement(operators,len(values)-1):
    #         for ops in set(permutations(combo,len(values)-1)):
    #             print("\t", ops)
    #             result = values[0]
    #             for i,op in enumerate(ops):
    #                 result = eval(f"{result} {op} {values[i+1]}")
    #                 if result > solution: break
    #             if result == solution:
    #                 part1 += result
    #                 break

    print(f"Day 07 | Part 1: {part1}      | {'Correct' if part1 == 5531 else 'Wrong'}")
            