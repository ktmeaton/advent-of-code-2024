#!/usr/bin/env python

import sys
import asyncio

async def main():

    if len(sys.argv) == 1:
        sys.exit(0)

    day = sys.argv[1]
    days = [day] if day != "all" else ["day" + i for i in ["01", "02", "03", "04", "05", "06"]]

    tasks = []
    for day in days:
        exec(f"from {day} import {day}", globals())
        task = eval(f"asyncio.create_task({day}())")
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        result = await task


if __name__ == "__main__":
    asyncio.run(main())

    
