import re


def get_rule(text, br):
    entry_bag = text.split("bags contain")[0].strip()
    if entry_bag not in br.keys():
        br[entry_bag] = {}
    for m in re.findall(r'(\d+) (\w+) (\w+) bag', text.split("bags contain")[1]):
        br[entry_bag][m[1] + ' ' + m[2]] = m[0]


def build_bag_tree(br):
    bags_content = {}
    for bag in br:
        bags_content[bag] = build_bag_tree_rec(br, bag, bags_content)
    return bags_content


def build_bag_tree_rec(br, bag, bags_content):
    if bag in bags_content.keys():
        return bags_content[bag]
    else:
        content = []
        for b in br[bag].keys():
            content.append(b)
            content.extend(build_bag_tree_rec(br, b, bags_content))
        return content


def get_nb_bags_rec(br, bag):
    if len(br[bag]) == 0:
        return 0
    else:
        count = 0
        for b in br[bag].keys():
            count += int(br[bag][b]) * (1 + get_nb_bags_rec(br, b))
    return count


filepath = "inputs/day7_input.txt"
with open(filepath, 'r') as f:
    lines = f.readlines()

# Part 1
bag_rules = {}
for line in lines:
    get_rule(line, bag_rules)
searched_bag = 'shiny gold'
bags_contents = build_bag_tree(bag_rules)
print(len([b for b in bags_contents.keys() if searched_bag in bags_contents[b]]))

# Part 2
print(get_nb_bags_rec(bag_rules, searched_bag))
