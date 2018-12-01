import os

DAY = 5

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()


def count_steps(s, two=False):

    steps = list(map(int, s.split('\n')))
    count = 0
    pos = 0
    while True:
        try:
            incr = steps[pos]
            steps[pos] += -1 if two and incr >= 3 else 1
            pos += incr
        except IndexError:
            return count
        count += 1


t = '0\n3\n0\n1\n-3'

assert count_steps(t) == 5

print("PART 1", count_steps(input_string))

assert count_steps(t, True) == 10

print("PART 2", count_steps(input_string, True))
