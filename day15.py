puzzle_input = [12, 20, 0, 6, 1, 17, 7]
# puzzle_input = [0,3,6]

cur_turn = 1
last_spoken_nb = 0
last_nb_turn = {}
for x in puzzle_input:
    last_nb_turn[x] = cur_turn
    last_spoken_nb = x
    cur_turn += 1

while cur_turn <= 30000000:
    if last_spoken_nb in last_nb_turn.keys():
        spoken_nb = cur_turn - 1 - last_nb_turn[last_spoken_nb]
        last_nb_turn[last_spoken_nb] = cur_turn - 1
        last_spoken_nb = spoken_nb
    else:
        last_nb_turn[last_spoken_nb] = cur_turn - 1
        last_spoken_nb = 0
    cur_turn += 1

print(last_spoken_nb)
