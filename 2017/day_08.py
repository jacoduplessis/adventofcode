import os

DAY = 8

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()


def get_max(s, two=False):
    register = {}
    maxima = []
    for line in s.split('\n'):
        key, op, val, _, left_key, comp, right = line.split()
        val = int(val)
        right = int(right)
        try:
            left = int(register[left_key])
        except KeyError:
            left = 0
        if comp == '>':
            b = left > right
        elif comp == '<':
            b = left < right
        elif comp == '!=':
            b = left != right
        elif comp == '==':
            b = left == right
        elif comp == '<=':
            b = left <= right
        elif comp == '>=':
            b = left >= right

        if not b:
            continue

        if key not in register:
            register[key] = 0

        if op == 'inc':
            register[key] += val
        else:
            register[key] -= val

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
