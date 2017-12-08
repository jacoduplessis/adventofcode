import os

DAY = 8

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()

from collections import defaultdict


def get_max(s, two=False):
    register = defaultdict(int)

    maxima = []
    for line in s.split('\n'):
        key, op, val, _, left_key, comp, right = line.split()
        val = int(val)
        right = int(right)
        left = int(register.get(left_key, 0))

        if not eval(f'{left} {comp} {right}'):
            continue

        register[key] += val if op == 'inc' else (-1 * val)
        maxima.append(max(register.values()))

    if two:
        return max(maxima)

    return max(register.values())


t = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

assert get_max(t) == 1
assert get_max(t, True) == 10

print("PART 1", get_max(input_string))
print("PART 2", get_max(input_string, True))
