
filepath = "inputs/day1_input.txt"
with open(filepath, "r") as f:
    f_list = f.readlines()
    num_list = [int(x) for x in f_list]
    for x in num_list:
        y = 2020 - x
        if y in num_list:
            print(x, y, x*y)
            break

    for x in num_list:
        find = False
        for y in [n for n in num_list if n < 2020 - x]:
            z = 2020 - x - y
            if z in num_list:
                print(x, y, z, x*y*z)
                find = True
                break
        if find:
            break
