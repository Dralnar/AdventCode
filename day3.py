def count_trees(matrix, step_x, step_y):
    x = 0
    y = 0
    nb_trees = 0
    tree_symbol = "#"
    while x < len(matrix):
        if (matrix[x][y % len(matrix[x])]) == tree_symbol:
            nb_trees += 1
        x += step_x
        y += step_y
    return nb_trees


filepath = "inputs/day3_input.txt"
with open(filepath, 'r') as f:
    m = [[s for s in line] for line in f.read().split('\n')]
nb11 = count_trees(m, 1, 1)
nb13 = count_trees(m, 1, 3)
nb15 = count_trees(m, 1, 5)
nb17 = count_trees(m, 1, 7)
nb21 = count_trees(m, 2, 1)
print(nb11)
print(nb13)
print(nb15)
print(nb17)
print(nb21)
print(nb11 * nb13 * nb15 * nb17 * nb21)
