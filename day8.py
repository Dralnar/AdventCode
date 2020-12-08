import re

filepath = "inputs/day8_input.txt"

with open(filepath, 'r') as f:
    lines = f.readlines()

# Part 1
acc = 0
line_re = r'^(\w{3}) (\+|-)(\d+)$'
i = 0
visited_lines = []
while i < len(lines):
    if i in visited_lines:
        break
    m = re.match(line_re, lines[i])
    visited_lines.append(i)
    if m:
        if m.group(1) == "nop":
            i += 1
        if m.group(1) == "acc":
            i += 1
            acc += int(m.group(3)) if m.group(2) == '+' else -int(m.group(3))
        if m.group(1) == "jmp":
            i += int(m.group(3)) if m.group(2) == '+' else -int(m.group(3))

print(acc)


# Part 2
def switch_opp(l):
    m1 = re.match(r'^(nop|jmp) .*$', l)
    if m1:
        if m1.group(1) == 'nop':
            return l.replace('nop', 'jmp')
        if m1.group(1) == 'jmp':
            return l.replace('jmp', 'nop')
    return l


j = 0
potential_switches = []
while j < len(lines):
    if re.match(r'^(nop|jmp) .*$', lines[j]):
        potential_switches.append(j)
    j += 1

for i in potential_switches:
    modified_lines = list(lines)
    modified_lines[i] = switch_opp(modified_lines[i])
    has_finished = True
    j = 0
    acc = 0
    visited_lines = []
    while j < len(modified_lines):
        if j in visited_lines:
            has_finished = False
            break
        m = re.match(line_re, modified_lines[j])
        visited_lines.append(j)
        if m:
            if m.group(1) == "nop":
                j += 1
            if m.group(1) == "acc":
                j += 1
                acc += int(m.group(3)) if m.group(2) == '+' else -int(m.group(3))
            if m.group(1) == "jmp":
                j += int(m.group(3)) if m.group(2) == '+' else -int(m.group(3))

    if has_finished:
        print(acc)
        break


