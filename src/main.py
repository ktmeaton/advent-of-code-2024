#!/usr/bin/env python

import sys

if __name__ == "__main__":

    day = sys.argv[1]

    days = [day] if day != "all" else ["day01","day02", "day03", "day04", "day05"]

    for day in days:
        try:
            exec(f"from {day} import {day}")
            exec(f"{day}()")
        except:
            ...

