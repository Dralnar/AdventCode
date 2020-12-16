import math

filepath = "inputs/day13_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()

# Part 1
earliest_time = int(lines[0])
bus_lines = set(lines[1].split(','))
bus_lines.remove('x')

next_dep = {}
for bl in bus_lines:
    if earliest_time % int(bl) != 0:
        next_dep[(math.floor(earliest_time/int(bl)) + 1) * int(bl)] = int(bl)
    else:
        next_dep[earliest_time] = int(bl)

earliest_bus = min(next_dep.keys())
print(next_dep[earliest_bus] * (earliest_bus - earliest_time))


# Part 2
bus_lines = {}
i = 0
for v in lines[1].split(','):
    if v != 'x':
        bus_lines[int(v)] = i
    i += 1
init_val = list(bus_lines.keys())[0]
max_val = max(bus_lines.keys())
max_index = bus_lines[max_val]
blk = list(bus_lines.keys())
blk.sort(reverse=True)
j = 1
is_found = False
while not is_found:
    is_the_one = True
    for k in blk:
        if ((j * max_val) + bus_lines[k] - max_index) % k != 0:
            is_the_one = False
            break
    if is_the_one:
        is_found = True
        print(init_val, j, init_val * j)
        break
    j += 1

