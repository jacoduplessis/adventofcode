import os

DAY = 7

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()

from collections import Counter


def parse_tree(s, two=False):
    nodes = {}
    for line in s.split('\n'):
        name, weight, *children = line.split(' ')
        weight = int(weight.strip('()'))
        children = [c.strip(',') for c in children if c != '->']
        nodes[name] = {
            'n': name,
            'c': children,
            'w': weight,
        }

    def get_total_weight(name):
        node = nodes[name]
        children = node.get('c')
        if children is None:
            return node['w'], True
        cw = [get_total_weight(c)[0] for c in children]
        return node['w'] + sum(cw), len(set(cw)) > 1, cw

    def get_level(name):
        node = nodes[name]
        children = node.get('c')
        if not children:
            return 0
        return 1 + get_level(children[0])

    def get_parent(name):
        for _, node in nodes.items():
            if name in node['c']:
                return node
        return None

    def get_delta(name):
        node = nodes[name]
        correct = Counter(node['cw']).most_common(1)[0][0]
        for weight, cname in zip(node['cw'], node['c']):
            if weight != correct:
                return weight - correct

    def get_error_node(name):
        node = nodes[name]
        if not node['e']:
            return name

        correct = Counter(node['cw']).most_common(1)[0][0]
        for weight, cname in zip(node['cw'], node['c']):
            if weight != correct:
                return get_error_node(cname)

    for name, node in nodes.items():
        node['l'] = get_level(name)
        node['tw'], node['e'], node['cw'] = get_total_weight(name)

    with_err = [node for name, node in nodes.items() if node['e']]
    root_err_node = min(with_err, key=lambda n: n['l'])

    err_node = get_error_node(root_err_node['n'])
    if two:
        return nodes[err_node]['w'] - get_delta(get_parent(err_node)['n'])
    return max(nodes.values(), key=lambda n: n['l']).get('n')


t = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".strip('\n').strip()

assert parse_tree(t) == 'tknk'
assert parse_tree(t, True) == 60

print("PART 1", parse_tree(input_string))
print("PART 2", parse_tree(input_string, True))
