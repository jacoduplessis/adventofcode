import pathlib


def top(depth, n):
    return n % (2 * (depth - 1)) == 0


def part_one(lines):
    score = 0
    layers = {}
    for line in lines:
        i, depth = line.split(': ')
        i = int(i)
        depth = int(depth)
        layers[i] = depth
    N = max(layers.keys()) + 1

    for mv in range(N):
        if mv not in layers:
            continue
        if top(layers[mv], mv):
            score += mv * layers[mv]

    return score


def part_two(lines):
    delay = 0
    layers = {}
    for line in lines:
        i, depth = line.split(': ')
        i = int(i)
        depth = int(depth)
        layers[i] = depth
    N = max(layers.keys()) + 1

    while True:
        delay += 1
        caught = False
        for mv in range(N):
            pico = mv + delay
            if mv not in layers:
                continue
            if top(layers[mv], pico):
                # print(delay, "caught at", mv)
                caught = True
        if not caught:
            return delay


if __name__ == '__main__':
    test = """
0: 3
1: 2
4: 4
6: 4
"""
    # lines = test.strip().split('\n')
    lines = pathlib.Path('13.txt').read_text().strip().split('\n')
    print(part_one(lines))
    print(part_two(lines))
