
filepath = "inputs/day10_input.txt"

with open(filepath, 'r') as f:
    lines = f.readlines()

# Part 1
adapter_list = []
for line in lines:
    adapter_list.append(int(line.strip()))

nb_1_jolt_diff = 0
nb_3_jolt_diff = 0
i = 0
while True:
    if i + 1 in adapter_list:
        nb_1_jolt_diff += 1
        i += 1
        continue
    elif i + 2 in adapter_list:
        i += 2
        continue
    elif i + 3 in adapter_list:
        nb_3_jolt_diff += 1
        i += 3
        continue
    else:
        break

nb_3_jolt_diff += 1
print(nb_1_jolt_diff)
print(nb_3_jolt_diff)
print(nb_1_jolt_diff * nb_3_jolt_diff)


# Part 2
sorted_adapter_list = adapter_list.copy()
sorted_adapter_list.sort(reverse=True)
adapters_path_dict = {}
for ad in sorted_adapter_list:
    adapters_path_dict[ad] = 0
    if ad + 1 not in sorted_adapter_list and ad + 2 not in sorted_adapter_list and ad + 3 not in sorted_adapter_list:
        adapters_path_dict[ad] = 1
    else:
        for x in [1, 2, 3]:
            if ad + x in sorted_adapter_list:
                adapters_path_dict[ad] += adapters_path_dict[ad + x]

first_adapter = 0
total_paths = 0
for x in [1, 2, 3]:
    if first_adapter + x in sorted_adapter_list:
        total_paths += adapters_path_dict[first_adapter + x]
print(total_paths)