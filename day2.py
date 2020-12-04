import re

filepath = "inputs/day2_input.txt"
with open(filepath, 'r') as f:
    list_pwd = f.readlines()
    total = 0
    for line in list_pwd:
        pwd_re = r'(\d+)-(\d+) (\w): (\w*)'
        m = re.match(pwd_re, line)
        if m:
            min_val = int(m.group(1))
            max_val = int(m.group(2))
            letter = m.group(3)
            pwd = m.group(4)
            if min_val <= pwd.count(letter) <= max_val:
                total += 1
    print(total)

    total2 = 0
    for line in list_pwd:
        pwd_re = r'(\d+)-(\d+) (\w): (\w*)'
        m = re.match(pwd_re, line)
        if m:
            pos1 = int(m.group(1))
            pos2 = int(m.group(2))
            letter = m.group(3)
            pwd = m.group(4)
            if (pwd[pos1-1] == letter and pwd[pos2-1] != letter) or (pwd[pos1-1] != letter and pwd[pos2-1] == letter):
                total2 += 1
    print(total2)


