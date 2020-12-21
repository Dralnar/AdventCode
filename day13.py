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
bus_lines = [[i, int(val)] for i, val in enumerate(lines[1].split(',')) if val != "x"]
cProd = 1
c = 0
for k in range(1, len(bus_lines)):
    a = 0
    cProd *= bus_lines[k-1][1]
    reste = c % bus_lines[k][1]
    while reste != (bus_lines[k][1] - bus_lines[k][0]) % bus_lines[k][1]:
        a += 1
        reste = (reste + cProd) % bus_lines[k][1]
    c += a*cProd
print(c)


