import re

filepath = "inputs/day14_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()

# Part 1
mask = []
mem = {}
for line in lines:
    m_mask = re.match(r'mask = (\w{36})', line)
    if m_mask:
        mask = [[i, val] for i, val in enumerate(m_mask.group(1)) if val != 'X']

    m_mem = re.match(r'mem\[(\d+)] = (\d+)', line)
    if m_mem:
        bin_val = list(format(int(m_mem.group(2)), '036b'))
        for j in range(0, len(mask)):
            bin_val[mask[j][0]] = mask[j][1]
        mem[int(m_mem.group(1))] = int(''.join(bin_val), 2)
s = 0
for k in mem.keys():
    s += mem[k]
print(s)


# Part 2
def explore_tree(mem_stack, bin_a, pos, val):
    if pos <= 35:
        if bin_a[pos] == 'X':
            cp = bin_a.copy()
            cp[pos] = '0'
            explore_tree(mem_stack, cp, pos + 1, val)
            cp[pos] = '1'
            explore_tree(mem_stack, cp, pos + 1, val)
        else:
            explore_tree(mem_stack, bin_a, pos + 1, val)
    elif pos == 36:
        mem_stack[int(''.join(bin_a), 2)] = val


mask = []
mem = {}
for line in lines:
    m_mask = re.match(r'mask = (\w{36})', line)
    if m_mask:
        mask = list(m_mask.group(1))

    m_mem = re.match(r'mem\[(\d+)] = (\d+)', line)
    if m_mem:
        bin_add = list(format(int(m_mem.group(1)), '036b'))
        for j in range(0, len(mask)):
            if mask[j] == '1' or mask[j] == 'X':
                bin_add[j] = mask[j]
        explore_tree(mem, bin_add, 0, int(m_mem.group(2)))
s = 0
for k in mem.keys():
    s += mem[k]
print(s)
