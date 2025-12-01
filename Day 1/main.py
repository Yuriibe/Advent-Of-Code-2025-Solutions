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
            start = (start + number) % 100
        else:
            start = (start - number) % 100
        if start == 0:
            counter = counter + 1
print(counter)
