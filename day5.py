import re
from math import floor


def get_seat_id(code):
    if len(code) != 10:
        return -1
    if not re.match(r'^[FB]{7}$', code[:7]):
        return -1
    if not re.match(r'^[LR]{3}$', code[7:]):
        return -1
    row = decode_seat(code[:7], 0, 127)
    seat = decode_seat(code[7:], 0, 7)
    return row * 8 + seat


def decode_seat(code, lower_limit, upper_limit):
    if len(code) > 1:
        if code[0] == "F" or code[0] == "L":
            return decode_seat(code[1:], lower_limit, floor((upper_limit + lower_limit + 1) / 2) - 1)
        if code[0] == "B" or code[0] == "R":
            return decode_seat(code[1:], floor((upper_limit + lower_limit + 1) / 2), upper_limit)
    else:
        if code[0] == "F" or code[0] == "L":
            return lower_limit
        if code[0] == "B" or code[0] == "R":
            return upper_limit


filepath = "inputs/day5_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()
seat_ids = []
for line in lines:
    seat_ids.append(get_seat_id(line.strip()))
print(max(seat_ids))

missing_seat = [x + 1 for x in seat_ids if x + 1 not in seat_ids and x != max(seat_ids)]
print(missing_seat)
