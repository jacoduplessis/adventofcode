import collections
import pathlib
import re


def part_one(input_):
    points = collections.defaultdict(int)
    part_two = None

    # #1 @ 817,273: 26x26
    claims = [
        re.match(r'#(?P<id>\d+)\s@\s(?P<ml>\d+),(?P<mt>\d+):\s(?P<px>\d+)x(?P<py>\d+)', line).groups()
        for line in input_]
    for line in claims:
        id_, ml, mt, x, y = line
        ml, mt, x, y = int(ml), int(mt), int(x), int(y)
        for i in range(x):
            xkey = ml + i
            for j in range(y):
                ykey = mt + j
                key = f'{xkey}x{ykey}'
                points[key] += 1

    n = 0
    for i in range(1_000):
        for j in range(1_000):
            if points[f'{i}x{j}'] >= 2:
                n += 1

    for line in claims:
        id_, ml, mt, x, y = line
        ml, mt, x, y = int(ml), int(mt), int(x), int(y)
        alone = True
        for i in range(x):
            xkey = ml + i
            for j in range(y):
                ykey = mt + j
                key = f'{xkey}x{ykey}'
                if points[key] != 1:
                    alone = False
        if alone:
            part_two = id_

    return n, part_two


if __name__ == '__main__':
    lines = pathlib.Path('03.txt').read_text().strip().split('\n')
    print(part_one(lines))
