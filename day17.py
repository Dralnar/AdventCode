from copy import deepcopy

filepath = "inputs/day17_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()
cube_active = '#'
cube_inactive = '.'


def count_active_cubes_around(m, x, y, z):
    count = 0
    if x > 0 and y > 0 and z > 0 and m[z-1][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and m[z][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and z < len(m)-1 and m[z+1][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and z > 0 and m[z-1][x-1][y] == cube_active:
        count += 1
    if x > 0 and m[z][x-1][y] == cube_active:
        count += 1
    if x > 0 and z < len(m)-1 and m[z+1][x-1][y] == cube_active:
        count += 1
    if x > 0 and y < len(m[z][x])-1 and z > 0 and m[z-1][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[z][x])-1 and m[z][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[z][x])-1 and z < len(m)-1 and m[z+1][x-1][y+1] == cube_active:
        count += 1
    if y > 0 and z > 0 and m[z-1][x][y-1] == cube_active:
        count += 1
    if y > 0 and m[z][x][y-1] == cube_active:
        count += 1
    if y > 0 and z < len(m)-1 and m[z+1][x][y-1] == cube_active:
        count += 1
    if y < len(m[z][x])-1 and z > 0 and m[z-1][x][y+1] == cube_active:
        count += 1
    if y < len(m[z][x])-1 and m[z][x][y+1] == cube_active:
        count += 1
    if y < len(m[z][x])-1 and z < len(m)-1 and m[z+1][x][y+1] == cube_active:
        count += 1
    if x < len(m[z])-1 and y > 0 and z > 0 and m[z-1][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[z])-1 and y > 0 and m[z][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[z])-1 and y > 0 and z < len(m)-1 and m[z+1][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[z])-1 and z > 0 and m[z-1][x+1][y] == cube_active:
        count += 1
    if x < len(m[z])-1 and m[z][x+1][y] == cube_active:
        count += 1
    if x < len(m[z])-1 and z < len(m)-1 and m[z+1][x+1][y] == cube_active:
        count += 1
    if x < len(m[z])-1 and y < len(m[z][x])-1 and z > 0 and m[z-1][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[z])-1 and y < len(m[z][x])-1 and m[z][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[z])-1 and y < len(m[z][x])-1 and z < len(m)-1 and m[z+1][x+1][y+1] == cube_active:
        count += 1
    if z > 0 and m[z-1][x][y] == cube_active:
        count += 1
    if z < len(m)-1 and m[z+1][x][y] == cube_active:
        count += 1
    return count


def count_active_cubes_around_bis(m, x, y, z, w):
    count = 0
    if x > 0 and y > 0 and z > 0 and w > 0 and m[w-1][z-1][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and z > 0 and m[w][z-1][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and z > 0 and w < len(m)-1 and m[w+1][z-1][x-1][y-1] == cube_active:
        count += 1

    if x > 0 and y > 0 and w > 0 and m[w-1][z][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and m[w][z][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and w < len(m)-1 and m[w+1][z][x-1][y-1] == cube_active:
        count += 1

    if x > 0 and y > 0 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and z < len(m[w])-1 and m[w][z+1][x-1][y-1] == cube_active:
        count += 1
    if x > 0 and y > 0 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x-1][y-1] == cube_active:
        count += 1

    if x > 0 and z > 0 and w > 0 and m[w-1][z-1][x-1][y] == cube_active:
        count += 1
    if x > 0 and z > 0 and m[w][z-1][x-1][y] == cube_active:
        count += 1
    if x > 0 and z > 0 and w < len(m)-1 and m[w+1][z-1][x-1][y] == cube_active:
        count += 1

    if x > 0 and w > 0 and m[w-1][z][x-1][y] == cube_active:
        count += 1
    if x > 0 and m[w][z][x-1][y] == cube_active:
        count += 1
    if x > 0 and w < len(m)-1 and m[w+1][z][x-1][y] == cube_active:
        count += 1

    if x > 0 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x-1][y] == cube_active:
        count += 1
    if x > 0 and z < len(m[w])-1 and m[w][z+1][x-1][y] == cube_active:
        count += 1
    if x > 0 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x-1][y] == cube_active:
        count += 1

    if x > 0 and y < len(m[w][z][x])-1 and z > 0 and w > 0 and m[w-1][z-1][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[w][z][x])-1 and z > 0 and m[w][z-1][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[w][z][x])-1 and z > 0 and w < len(m)-1 and m[w+1][z-1][x-1][y+1] == cube_active:
        count += 1

    if x > 0 and y < len(m[w][z][x])-1 and w > 0 and m[w-1][z][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[w][z][x])-1 and m[w][z][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[w][z][x])-1 and w < len(m)-1 and m[w+1][z][x-1][y+1] == cube_active:
        count += 1

    if x > 0 and y < len(m[w][z][x])-1 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[w][z][x])-1 and z < len(m[w])-1 and m[w][z+1][x-1][y+1] == cube_active:
        count += 1
    if x > 0 and y < len(m[w][z][x])-1 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x-1][y+1] == cube_active:
        count += 1

    if y > 0 and z > 0 and w > 0 and m[w-1][z-1][x][y-1] == cube_active:
        count += 1
    if y > 0 and z > 0 and m[w][z-1][x][y-1] == cube_active:
        count += 1
    if y > 0 and z > 0 and w < len(m)-1 and m[w+1][z-1][x][y-1] == cube_active:
        count += 1

    if y > 0 and w > 0 and m[w-1][z][x][y-1] == cube_active:
        count += 1
    if y > 0 and m[w][z][x][y-1] == cube_active:
        count += 1
    if y > 0 and w < len(m)-1 and m[w+1][z][x][y-1] == cube_active:
        count += 1

    if y > 0 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x][y-1] == cube_active:
        count += 1
    if y > 0 and z < len(m[w])-1 and m[w][z+1][x][y-1] == cube_active:
        count += 1
    if y > 0 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x][y-1] == cube_active:
        count += 1

    if y < len(m[w][z][x])-1 and z > 0 and w > 0 and m[w-1][z-1][x][y+1] == cube_active:
        count += 1
    if y < len(m[w][z][x])-1 and z > 0 and m[w][z-1][x][y+1] == cube_active:
        count += 1
    if y < len(m[w][z][x])-1 and z > 0 and w < len(m)-1 and m[w+1][z-1][x][y+1] == cube_active:
        count += 1

    if y < len(m[w][z][x])-1 and w > 0 and m[w-1][z][x][y+1] == cube_active:
        count += 1
    if y < len(m[w][z][x])-1 and m[w][z][x][y+1] == cube_active:
        count += 1
    if y < len(m[w][z][x])-1 and w < len(m)-1 and m[w+1][z][x][y+1] == cube_active:
        count += 1

    if y < len(m[w][z][x])-1 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x][y+1] == cube_active:
        count += 1
    if y < len(m[w][z][x])-1 and z < len(m[w])-1 and m[w][z+1][x][y+1] == cube_active:
        count += 1
    if y < len(m[w][z][x])-1 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x][y+1] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and y > 0 and z > 0 and w > 0 and m[w-1][z-1][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y > 0 and z > 0 and m[w][z-1][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y > 0 and z > 0 and w < len(m)-1 and m[w+1][z-1][x+1][y-1] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and y > 0 and w > 0 and m[w-1][z][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y > 0 and m[w][z][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y > 0 and w < len(m)-1 and m[w+1][z][x+1][y-1] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and y > 0 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y > 0 and z < len(m[w])-1 and m[w][z+1][x+1][y-1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y > 0 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x+1][y-1] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and z > 0 and w > 0 and m[w-1][z-1][x+1][y] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and z > 0 and m[w][z-1][x+1][y] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and z > 0 and w < len(m)-1 and m[w+1][z-1][x+1][y] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and w > 0 and m[w-1][z][x+1][y] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and m[w][z][x+1][y] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and w < len(m)-1 and m[w+1][z][x+1][y] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x+1][y] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and z < len(m[w])-1 and m[w][z+1][x+1][y] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x+1][y] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and z > 0 and w > 0 and m[w-1][z-1][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and z > 0 and m[w][z-1][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and z > 0 and w < len(m)-1 and m[w+1][z-1][x+1][y+1] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and w > 0 and m[w-1][z][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and m[w][z][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and w < len(m)-1 and m[w+1][z][x+1][y+1] == cube_active:
        count += 1

    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and z < len(m[w])-1 and w > 0 and m[w-1][z+1][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and z < len(m[w])-1 and m[w][z+1][x+1][y+1] == cube_active:
        count += 1
    if x < len(m[w][z])-1 and y < len(m[w][z][x])-1 and z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x+1][y+1] == cube_active:
        count += 1

    if z > 0 and w > 0 and m[w-1][z-1][x][y] == cube_active:
        count += 1
    if z > 0 and m[w][z-1][x][y] == cube_active:
        count += 1
    if z > 0 and w < len(m)-1 and m[w+1][z-1][x][y] == cube_active:
        count += 1

    if z < len(m[w])-1 and w > 0 and m[w-1][z+1][x][y] == cube_active:
        count += 1
    if z < len(m[w])-1 and m[w][z+1][x][y] == cube_active:
        count += 1
    if z < len(m[w])-1 and w < len(m)-1 and m[w+1][z+1][x][y] == cube_active:
        count += 1

    if w > 0 and m[w-1][z][x][y] == cube_active:
        count += 1
    if w < len(m)-1 and m[w][z][x][y] == cube_active:
        count += 1

    return count


def change_state(m, x, y, z):
    value = m[z][x][y]
    new_value = value
    if value == cube_active and count_active_cubes_around(m, x, y, z) != 2 and count_active_cubes_around(m, x, y, z) != 3:
        new_value = cube_inactive
    elif value == cube_inactive and count_active_cubes_around(m, x, y, z) == 3:
        new_value = cube_active
    return new_value


def change_state_bis(m, x, y, z, w):
    value = m[w][z][x][y]
    new_value = value
    if value == cube_active and count_active_cubes_around_bis(m, x, y, z, w) != 2 and count_active_cubes_around_bis(m, x, y, z, w) != 3:
        new_value = cube_inactive
    elif value == cube_inactive and count_active_cubes_around_bis(m, x, y, z, w) == 3:
        new_value = cube_active
    return new_value


def count_cube_state(m, state):
    count = 0
    for z in range(0, len(m)):
        for x in range(0, len(m[z])):
            count += len([y for y in m[z][x] if y == state])
    return count


def count_cube_state_bis(m, state):
    count = 0
    for w in range(len(m)):
        for z in range(len(m[w])):
            for x in range(len(m[w][z])):
                count += len([y for y in m[w][z][x] if y == state])
    return count


# Part 1
cube_matrix = []
cube_matrix.insert(0, [])
for line in lines:
    cube_matrix[0].append(list(line.strip()))

# has_changed = True
round_nb = 0
while round_nb < 6:
    # has_changed = False
    for plan in cube_matrix:
        for row in plan:
            row.append(cube_inactive)
            row.insert(0, cube_inactive)
        plan.append([cube_inactive for i in range(len(plan[0]))])
        plan.insert(0, [cube_inactive for i in range(len(plan[0]))])
    cube_matrix.append([[cube_inactive for i in range(len(cube_matrix[0][0]))] for j in range(0, len(cube_matrix[0]))])
    cube_matrix.insert(0, [[cube_inactive for i in range(len(cube_matrix[0][0]))] for j in range(0, len(cube_matrix[0]))])

    cube_matrix_copy = deepcopy(cube_matrix)
    for k in range(0, len(cube_matrix)):
        for i in range(0, len(cube_matrix[k])):
            for j in range(0, len(cube_matrix[k][i])):
                cube_matrix_copy[k][i][j] = change_state(cube_matrix, i, j, k)
    cube_matrix = cube_matrix_copy
    round_nb += 1

    # print("Round {0} : {1} inactive and {2} active cubes".format(round_nb, count_cube_state(cube_matrix, cube_inactive), count_cube_state(cube_matrix, cube_active)))
print(count_cube_state(cube_matrix, cube_active))

# Part 2
print('part2')
cube_matrix = []
cube_matrix.insert(0, [])
cube_matrix[0].insert(0, [])
for line in lines:
    cube_matrix[0][0].append(list(line.strip()))

# has_changed = True
round_nb = 0
while round_nb < 6:
    # has_changed = False
    for dim in cube_matrix:
        for plan in dim:
            for row in plan:
                row.append(cube_inactive)
                row.insert(0, cube_inactive)
            plan.append([cube_inactive for i in range(len(plan[0]))])
            plan.insert(0, [cube_inactive for i in range(len(plan[0]))])
        dim.append([[cube_inactive for i in range(len(dim[0][0]))] for j in range(0, len(dim[0]))])
        dim.insert(0, [[cube_inactive for i in range(len(dim[0][0]))] for j in range(0, len(dim[0]))])
    cube_matrix.append([[[cube_inactive for i in range(len(cube_matrix[0][0][0]))] for j in range(len(cube_matrix[0][0]))] for k in range(len(cube_matrix[0]))])
    cube_matrix.insert(0, [[[cube_inactive for i in range(len(cube_matrix[0][0][0]))] for j in range(len(cube_matrix[0][0]))] for k in range(len(cube_matrix[0]))])

    cube_matrix_copy = deepcopy(cube_matrix)
    for l in range(len(cube_matrix)):
        for k in range(len(cube_matrix[l])):
            for i in range(len(cube_matrix[l][k])):
                for j in range(len(cube_matrix[l][k][i])):
                    cube_matrix_copy[l][k][i][j] = change_state_bis(cube_matrix, i, j, k, l)
    cube_matrix = cube_matrix_copy
    round_nb += 1

    # print("Round {0} : {1} inactive and {2} active cubes".format(round_nb, count_cube_state(cube_matrix, cube_inactive), count_cube_state(cube_matrix, cube_active)))
    # for k in cube_matrix:
    #     for i in k:
    #         print(i)
    #     print("")
print(count_cube_state(cube_matrix, cube_active))
