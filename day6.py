
filepath = "inputs/day6_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()

# Part 1
yes_count = 0
last_line_empty = False
ans_list = []
for line in lines:
    if line == "\n":
        ans_list = list(dict.fromkeys(ans_list))
        yes_count += len(ans_list)
        ans_list = []
        last_line_empty = True
    else:
        ans_list.extend(list(line[:-1]))
        last_line_empty = False
if not last_line_empty:
    ans_list = list(dict.fromkeys(ans_list))
    yes_count += len(ans_list)
print(yes_count)

# Part 2
yes_count = 0
last_line_empty = False
ans_dict = {}
i = 0
for line in lines:
    if line == "\n":
        ans_left = list(ans_dict[0])
        if len(ans_dict.keys()) >= 1:
            for s in ans_dict[0]:
                for j in [k for k in ans_dict.keys() if k != 0]:
                    if s not in ans_dict[j]:
                        ans_left.remove(s)
                        break
        yes_count += len(ans_left)
        ans_dict = {}
        last_line_empty = True
        i = 0
    else:
        ans_dict[i] = list(line[:-1])
        i += 1
        last_line_empty = False
if not last_line_empty:
    ans_left = list(ans_dict[0])
    if len(ans_dict.keys()) >= 1:
        for s in ans_dict[0]:
            for j in [k for k in ans_dict.keys() if k != 0]:
                if s not in ans_dict[j]:
                    ans_left.remove(s)
                    break
    yes_count += len(ans_left)
print(yes_count)
