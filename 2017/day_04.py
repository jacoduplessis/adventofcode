import os

DAY = 4

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()

from collections import Counter


def count_valid(s):
    lines = s.split('\n')
    valid = 0
    for line in lines:
        words = map(str.strip, line.split(' '))
        c = Counter(words)
        if c.most_common(1)[0][1] == 1:
            valid += 1

    return valid


def part_2(s):
    lines = s.split('\n')
    valid = 0
    for line in lines:
        d = {}
        words = map(str.strip, line.split(' '))
        invalid = False
        for w in words:
            sorted_letters = ''.join(sorted(w))
            if sorted_letters in d:
                invalid = True
            d[sorted_letters] = 1

        if not invalid:
            valid += 1

    return valid


print("PART 1", count_valid(input_string))

assert part_2("abcde fghij") == 1
assert part_2("abcde xyz ecdab") == 0

print("PART 2", part_2(input_string))
