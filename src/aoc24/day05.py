#!/usr/bin/env python3

def check_order(update, graph):
    correct = True
    for i in range(0, len(update)-1):
        page, next_page = update[i], update[i+1]
        if next_page not in graph[page]["children"]:
            correct = False
            break
    return correct

def fix_order(update, graph):
    correct = update[0:1]
    for page_u in update:
        if page_u in correct: continue
        for i, page_c in enumerate(correct):
            next_page = correct[i+1] if i < len(correct) - 1 else None
            if page_c in graph[page_u]["children"]:
                correct.insert(i, page_u)
                break
            elif not next_page and page_u in graph[page_c]["children"]:
                correct.insert(i+1, page_u)
                break
            # In between
            elif next_page and page_u in graph[page_c]["children"] and next_page in graph[page_u]["children"]:
                correct.insert(i+1, page_u)
                break
    return correct

async def day05():
    """ Printing pages in the correct order."""
    from collections import OrderedDict
    import math

    part1, part2 = 0, 0
    graph = OrderedDict()
    updates = []
    with open("data/day05.txt") as infile:
        lines = [line.strip() for line in infile]
    for line in lines:
        if "|" in line:
            parent, child = [int(l) for l in line.split("|")]
            if parent not in graph:
                graph[parent] = {"children": []}
            graph[parent]["children"].append(child)
            if child not in graph:
                graph[child] = {"children": []}
        if "," in line:
            u = [int(l) for l in line.split(",")]
            updates.append(u)

    incorrect = []
    for update in updates:
        if check_order(update, graph):
            part1 += update[math.floor(len(update) / 2)]
        else:
            fixed = fix_order(update, graph)
            part2 += fixed[math.floor(len(fixed) / 2)]

    print(f"Day 05 | Part 1: {part1}      | {'Correct' if part1 == 5391 else 'Wrong'}")
    print(f"       | Part 2: {part2}      | {'Correct' if part2 == 6142 else 'Wrong'}")

if __name__ == "__main__":
    day05()