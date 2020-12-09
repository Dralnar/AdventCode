
filepath = "inputs/day9_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()


def has_summable_nb(l, v):
    for x in l:
        l2 = list(l)
        l2.remove(x)
        if v in [x + y for y in l2]:
            return True
    return False


# Part 1
fifo_list = []
weakness = 0
for line in lines:
    value = int(line.strip())
    if len(fifo_list) < 25:
        fifo_list.append(value)
    else:
        if has_summable_nb(fifo_list, value):
            fifo_list.pop(0)
            fifo_list.append(value)
        else:
            weakness = value
            break

print(weakness)

# Part 2
weakness_list = []
for line in lines:
    if int(line.strip()) < weakness:
        weakness_list.append(int(line.strip()))
    else:
        break
i = 0
while i < len(weakness_list):
    j = i + 1
    x = weakness_list[i]
    x_sum = x
    add_list = [x]
    while j < len(weakness_list):
        y = weakness_list[j]
        if x_sum + y == weakness:
            add_list.append(y)
            break
        elif x_sum + y < weakness:
            x_sum += y
            add_list.append(y)
            j += 1
        elif x_sum + y > weakness:
            break
    if x_sum + weakness_list[j] == weakness:
        print(min(add_list) + max(add_list))
        break
    i += 1
