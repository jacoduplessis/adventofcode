import os

DAY = 1

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()


def get_captcha(s, halfway=False):
    nums = list(map(int, s))
    N = len(nums)
    step = int(N / 2) if halfway else 1
    return sum([nums[i] for i in range(N) if nums[i] == nums[(i + step) % N]])


# part 1
assert get_captcha('1122') == 3
assert get_captcha('1111') == 4
assert get_captcha('1234') == 0
assert get_captcha('91212129') == 9

print("PART 1", get_captcha(input_string))

# part 2
assert get_captcha('1212', True) == 6
assert get_captcha('1221', True) == 0
assert get_captcha('123425', True) == 4
assert get_captcha('123123', True) == 12
assert get_captcha('12131415', True) == 4

print("PART 2", get_captcha(input_string, True))
