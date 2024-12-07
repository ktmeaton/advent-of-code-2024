#!/usr/bin/env python

import sys
import asyncio

async def main():

    day = sys.argv[1]
    days = [day] if day != "all" else ["day01","day02", "day03", "day04", "day05"]
    tasks = []
    for day in days:
        exec(f"from {day} import {day}", globals())
        task = eval(f"asyncio.create_task({day}())")
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        _result = await task

if __name__ == "__main__":
    asyncio.run(main())
