import pathlib
from collections import Counter


def part_one(input_):
    twos = 0
    threes = 0
    for line in input_:
        c = Counter(line)
        has_two = False
        has_three = False
        for k, v in c.items():
            if v == 2:
                has_two = True
            if v == 3:
                has_three = True

        if has_three:
            threes += 1
        if has_two:
            twos += 1

    return twos * threes


def part_two(input_):
    N = len(input_)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            diffs = 0
            for k in range(len(input_[i])):
                if input_[i][k] != input_[j][k]:
                    diffs += 1

            if diffs == 1:
                match_chars = []
                for k in range(len(input_[i])):
                    if input_[i][k] == input_[j][k]:
                        match_chars.append(input_[i][k])

                return "".join(match_chars)


if __name__ == '__main__':
    lines = pathlib.Path('02.txt').read_text().strip().split('\n')
    print(part_one(lines))
    print(part_two(lines))
