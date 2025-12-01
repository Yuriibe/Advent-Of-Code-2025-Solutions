"""
Advent of Code Day 1: Secret Entrance
"""

import re

start = 50
counter = 0

with open("input") as f:
    for line in f:
        line = line.strip()
        m = re.match(r"([A-Za-z])(\d{1,3})", line)
        if m:
            letter = m.group(1)
            number = int(m.group(2))

            if letter == "R":
                count_zeros = (start + number) // 100
                counter += count_zeros
                start = (start + number) % 100
            else:
                if start == 0:
                    count_zeros = (number - 1) // 100
                elif number >= start:
                    count_zeros = (number - start) // 100 + 1
                else:
                    count_zeros = 0
                counter += count_zeros
                start = (start - number) % 100

print(f"Total zero crossings: {counter}")