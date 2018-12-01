import pathlib


def part_one(input_):
    n = 0
    for line in input_:
        operator, number = line[0], int(line[1:])
        n = n + number if operator == '+' else n - number
    return n


def part_two(input_):
    store = {}
    i = 0
    N = len(input_)
    n = 0
    while True:
        i = i % N
        operator, number = input_[i][0], int(input_[i][1:])
        n = n + number if operator == '+' else n - number
        if n in store:
            return n
        store[n] = True
        i += 1


if __name__ == '__main__':
    lines = pathlib.Path('01.txt').read_text().strip().split('\n')
    print(part_one(lines))
    print(part_two(lines))
