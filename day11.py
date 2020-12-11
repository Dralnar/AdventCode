from copy import deepcopy

filepath = "inputs/day11_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()
empty_seat = 'L'
occupied_seat = '#'
no_seat = '.'


def is_seat(seat):
    if seat == no_seat:
        return False
    else:
        return True


def count_occupied_seat_around(m, x, y):
    count = 0
    if x > 0 and y > 0 and m[x-1][y-1] == occupied_seat:
        count += 1
    if x > 0 and m[x-1][y] == occupied_seat:
        count += 1
    if x > 0 and y < len(m[x])-1 and m[x-1][y+1] == occupied_seat:
        count += 1
    if y > 0 and m[x][y-1] == occupied_seat:
        count += 1
    if y < len(m[x])-1 and m[x][y+1] == occupied_seat:
        count += 1
    if x < len(m)-1 and y > 0 and m[x+1][y-1] == occupied_seat:
        count += 1
    if x < len(m)-1 and m[x+1][y] == occupied_seat:
        count += 1
    if x < len(m)-1 and y < len(m[x])-1 and m[x+1][y+1] == occupied_seat:
        count += 1
    return count


def count_occupied_seat_visible(m, x, y):
    count = 0
    for d in range(0, 8):
        if next_seat_visible(m, x, y, d) == occupied_seat:
            count += 1
    return count


def next_seat_visible(m, x, y, d):
    """
    d = direction
    0 : upper left | 1 : upper center | 2 : upper right | 3 : center left | 4 : center right | 5 : lower left | 6 : lower center | 7 : lower right
    """
    if d == 0:
        if x > 0 and y > 0:
            if m[x-1][y-1] != no_seat:
                return m[x-1][y-1]
            else:
                return next_seat_visible(m, x-1, y-1, d)
        else:
            return no_seat
    if d == 1:
        if x > 0:
            if m[x-1][y] != no_seat:
                return m[x-1][y]
            else:
                return next_seat_visible(m, x-1, y, d)
        else:
            return no_seat
    if d == 2:
        if x > 0 and y < len(m[x])-1:
            if m[x-1][y+1] != no_seat:
                return m[x-1][y+1]
            else:
                return next_seat_visible(m, x-1, y+1, d)
        else:
            return no_seat
    if d == 3:
        if y > 0:
            if m[x][y-1] != no_seat:
                return m[x][y-1]
            else:
                return next_seat_visible(m, x, y-1, d)
        else:
            return no_seat
    if d == 4:
        if y < len(m[x])-1:
            if m[x][y+1] != no_seat:
                return m[x][y+1]
            else:
                return next_seat_visible(m, x, y+1, d)
        else:
            return no_seat
    if d == 5:
        if x < len(m)-1 and y > 0:
            if m[x+1][y-1] != no_seat:
                return m[x+1][y-1]
            else:
                return next_seat_visible(m, x+1, y-1, d)
        else:
            return no_seat
    if d == 6:
        if x < len(m)-1:
            if m[x+1][y] != no_seat:
                return m[x+1][y]
            else:
                return next_seat_visible(m, x+1, y, d)
        else:
            return no_seat
    if d == 7:
        if x < len(m)-1 and y < len(m[x])-1:
            if m[x+1][y+1] != no_seat:
                return m[x+1][y+1]
            else:
                return next_seat_visible(m, x+1, y+1, d)
        else:
            return no_seat
    return no_seat


def change_seat(m, x, y):
    value = m[x][y]
    new_value = value
    if value == empty_seat and count_occupied_seat_around(m, x, y) == 0:
        new_value = occupied_seat
    elif value == occupied_seat and count_occupied_seat_around(m, x, y) >= 4:
        new_value = empty_seat
    if new_value != value:
        return True, new_value
    else:
        return False, new_value


def change_seat_bis(m, x, y):
    value = m[x][y]
    new_value = value
    if value == empty_seat and count_occupied_seat_visible(m, x, y) == 0:
        new_value = occupied_seat
    elif value == occupied_seat and count_occupied_seat_visible(m, x, y) >= 5:
        new_value = empty_seat
    if new_value != value:
        return True, new_value
    else:
        return False, new_value


def count_seats(m, state):
    count = 0
    for x in range(0, len(m)):
        count += len([y for y in m[x] if y == state])
    return count


# Part 1
seat_matrix = []
for line in lines:
    seat_matrix.append(list(line.strip()))

has_changed = True
round_nb = 0
while has_changed:
    has_changed = False
    seat_matrix_copy = deepcopy(seat_matrix)
    for i in range(0, len(seat_matrix)):
        for j in range(0, len(seat_matrix[i])):
            if is_seat(seat_matrix[i][j]):
                seat_changed, val = change_seat(seat_matrix, i, j)
                if seat_changed:
                    has_changed = True
                    seat_matrix_copy[i][j] = val
    seat_matrix = seat_matrix_copy
    round_nb += 1
    # print("Round {0} : {1} empty and {2} occupied seats ({3} no seat)".format(round_nb, count_seats(seat_matrix, empty_seat), count_seats(seat_matrix, occupied_seat), count_seats(seat_matrix, no_seat)))

print(count_seats(seat_matrix, occupied_seat))

# Part 2
seat_matrix = []
for line in lines:
    seat_matrix.append(list(line.strip()))

has_changed = True
round_nb = 0
while has_changed:
    has_changed = False
    seat_matrix_copy = deepcopy(seat_matrix)
    for i in range(0, len(seat_matrix)):
        for j in range(0, len(seat_matrix[i])):
            if is_seat(seat_matrix[i][j]):
                seat_changed, val = change_seat_bis(seat_matrix, i, j)
                if seat_changed:
                    has_changed = True
                    seat_matrix_copy[i][j] = val
    seat_matrix = seat_matrix_copy
    round_nb += 1
    # print("Round {0} : {1} empty and {2} occupied seats ({3} no seat)".format(round_nb, count_seats(seat_matrix, empty_seat), count_seats(seat_matrix, occupied_seat), count_seats(seat_matrix, no_seat)))
print(count_seats(seat_matrix, occupied_seat))
