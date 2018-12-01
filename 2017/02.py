import os

DAY = 2

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()

import re


def get_checksum(s):
    total = 0
    for line in s.split('\n'):
        nums = sorted(map(int, re.findall(r'([\d]+)', line)))
        total += nums[-1] - nums[0]
    return total


def get_division(s):
    total = 0
    for line in s.split('\n'):
        nums = sorted(map(int, re.findall(r'([\d]+)', line)))

        # use function to easily break double loop
        def get_result(x):
            for i in range(len(x)):
                for j in range(len(x)):
                    if i != j and x[i] % x[j] == 0:
                        return int(x[i] / x[j])

        total += get_result(nums)
    return total


# part 1
assert get_checksum("5 1 9 5\n7 5 3\n2 4 6 8") == 18
print("PART 1", get_checksum(input_string))

# part 2
assert get_division("5 9 2 8\n9 4 7 3\n3 8 6 5") == 9
print("PART 2", get_division(input_string))
