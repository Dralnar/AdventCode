from itertools import chain
import re

filepath = "inputs/day16_input.txt"

with open(filepath, 'r') as f:
    lines = f.readlines()

rule_re = r'^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$'
mticket_re = r'^your ticket:$'
nticket_re = r'^nearby tickets:$'
rule_section = True
mt_section = False
nt_section = False
my_ticket = []
nearby_tickets = []
total_range = set()
rules_dict = {}

for line in lines:
    if rule_section:
        if re.match(mticket_re, line):
            rule_section = False
            mt_section = True
        else:
            m_rule = re.match(rule_re, line)
            if m_rule:
                total_range = total_range.union(set(list(chain(range(int(m_rule.group(2)), int(m_rule.group(3)) + 1), range(int(m_rule.group(4)), int(m_rule.group(5)) + 1)))))
                rules_dict[m_rule.group(1)] = set(list(chain(range(int(m_rule.group(2)), int(m_rule.group(3)) + 1), range(int(m_rule.group(4)), int(m_rule.group(5)) + 1))))
    elif mt_section:
        if re.match(nticket_re, line):
            mt_section = False
            nt_section = True
        elif line.strip():
            my_ticket = line.strip().split(',')
    elif nt_section:
        nearby_tickets.append(line.strip().split(','))

s = 0
for ticket in nearby_tickets:
    for value in ticket:
        if int(value) not in list(total_range):
            s += int(value)

print(s)

# Part 2
valid_tickets = []
for ticket in nearby_tickets:
    is_valid = True
    for value in ticket:
        if int(value) not in list(total_range):
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket)

fields_position = {}
possible_pos = {}
remaining_fields = list(rules_dict.keys())
for j in range(0, len(my_ticket)):
    for field in remaining_fields:
        field_ok = True
        for i in range(0, len(valid_tickets)):
            if int(valid_tickets[i][j]) not in rules_dict[field]:
                field_ok = False
                break
        if field_ok:
            if field in possible_pos.keys() and possible_pos[field]:
                possible_pos[field].append(j)
            else:
                possible_pos[field] = [j]

while len(remaining_fields) > 0:
    for field in remaining_fields:
        if len(possible_pos[field]) == 1:
            fields_position[field] = possible_pos[field][0]
            remaining_fields.remove(field)
            for f in remaining_fields:
                if possible_pos[field][0] in possible_pos[f]:
                    possible_pos[f].remove(possible_pos[field][0])

res = 1
for field in fields_position:
    if field.startswith('departure'):
        res *= int(my_ticket[fields_position[field]])

print(res)
