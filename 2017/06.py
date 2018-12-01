import os

DAY = 6

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()


def count_cycles(s, two=False):
    blocks = list(map(int, s.split()))
    banks = len(blocks)
    seen = set()
    count = 1
    repeating = None
    loop_count = None
    while True:

        dist = max(blocks)
        pos = blocks.index(dist)
        blocks[pos] = 0
        for i in range(1, dist + 1):
            blocks[(pos + i) % banks] += 1
        h = hash("".join(map(str, blocks)))
        if h in seen:
            if repeating is None:
                repeating = h
                loop_count = 0
            else:
                if h == repeating:
                    return loop_count
            if not two:
                return count
        seen.add(h)
        count += 1
        if repeating is not None:
            loop_count += 1


assert count_cycles("0 2 7 0") == 5

print("PART 1", count_cycles(input_string))

assert count_cycles("0 2 7 0", True) == 4

print("PART 2", count_cycles(input_string, True))
