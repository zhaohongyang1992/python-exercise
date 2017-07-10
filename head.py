#! /usr/bin/env python3

"""usage: cat test | ./head.py 4

"""

import sys

try:
    output_num = int(sys.argv[1])
except IOError as msg:
    output_num = 5

lines = sys.stdin.read().strip()
line_list = lines.split('\n')

for line in line_list[0:output_num]:
    print(line)
