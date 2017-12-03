import os

DAY = 3

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'input/{DAY}.txt'), 'r') as input_file:
    input_string = input_file.read().strip('\n').strip()

U, D, R, L = 1j, -1j, 1, -1
headings = [U, L, D, R]  # counter-clockwise


def distance(p):
    return int(abs(p.real) + abs(p.imag))


def generate_grid_points():
    ring = 0
    location = -1
    yield 0
    while True:
        ring += 1
        location += R
        steps = (ring - 1) * 2
        for heading in headings:
            for i in range(steps):
                if heading == U and i == 0:
                    yield location
                else:
                    location += heading
                    yield location


def get_distance(x):
    g = generate_grid_points()
    for i in range(x):
        p = next(g)
        if i + 1 == x:
            return distance(p)


assert get_distance(1) == 0
assert get_distance(12) == 3
assert get_distance(23) == 2
assert get_distance(1024) == 31

print("PART 1", get_distance(int(input_string)))


def part_two(target):
    g = generate_grid_points()
    n = 100
    center = int((n - 1) / 2)
    grid = []
    for i in range(n):
        grid.append([0 for _ in range(n)])
    grid[center][center] = 1
    while True:
        p = next(g)
        x = int(p.real + center)
        y = int(p.imag + center)
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                total += grid[x + i][y + j]
        if total > target:
            return total
        grid[x][y] = total


assert part_two(200) == 304
assert part_two(700) == 747

print("PART 2", part_two(int(input_string)))
