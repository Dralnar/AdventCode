import re
from copy import deepcopy

filepath = "inputs/day12_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()


# Part 1
# directions : North = 0 / East = 1 / South = 2 / West = 3
current_dir = 1
x = 0
y = 0
for line in lines:
    m = re.match(r'(\w)(\d+)', line)
    if m:
        if m.group(1) == 'L':
            current_dir = (current_dir - int(m.group(2)) / 90) % 4
        elif m.group(1) == 'R':
            current_dir = (current_dir + int(m.group(2)) / 90) % 4
        elif m.group(1) == 'F':
            if current_dir == 0:
                y += int(m.group(2))
            if current_dir == 1:
                x += int(m.group(2))
            if current_dir == 2:
                y -= int(m.group(2))
            if current_dir == 3:
                x -= int(m.group(2))
        elif m.group(1) == 'N':
            y += int(m.group(2))
        elif m.group(1) == 'E':
            x += int(m.group(2))
        elif m.group(1) == 'S':
            y -= int(m.group(2))
        elif m.group(1) == 'W':
            x -= int(m.group(2))

print(abs(x) + abs(y))

# Part 2
x = 0
y = 0
w_x = 10
w_y = 1
for line in lines:
    m = re.match(r'(\w)(\d+)', line)
    if m:
        if m.group(1) == 'L':
            nb_mv = int(int(m.group(2)) / 90)
            for i in range(0, nb_mv):
                tmp = w_y
                w_y = w_x
                w_x = - tmp
        elif m.group(1) == 'R':
            nb_mv = int(int(m.group(2)) / 90)
            for i in range(0, nb_mv):
                tmp = w_x
                w_x = w_y
                w_y = - tmp
        elif m.group(1) == 'F':
            for i in range(0, int(m.group(2))):
                x += w_x
                y += w_y
        elif m.group(1) == 'N':
            w_y += int(m.group(2))
        elif m.group(1) == 'E':
            w_x += int(m.group(2))
        elif m.group(1) == 'S':
            w_y -= int(m.group(2))
        elif m.group(1) == 'W':
            w_x -= int(m.group(2))

print(abs(x) + abs(y))
