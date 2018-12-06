import pathlib


def distance(p):
    return int(abs(p.real) + abs(p.imag))


def problem(lines):
    points = []
    for line in lines:
        x, y = line.split(', ')
        x = int(x)
        y = int(y)
        points.append(complex(x, y))

    l = int(min(points, key=lambda z: z.real).real)
    r = int(max(points, key=lambda z: z.real).real)
    t = int(max(points, key=lambda z: z.imag).imag)
    b = int(min(points, key=lambda z: z.imag).imag)

    def closest(p):
        min_d = 999
        min_p = None
        for pt in points:
            d = distance(pt-p)
            if d < min_d:
                min_d = d
                min_p = pt
            elif d == min_d:
                min_p = None
        return min_p

    grid = {}
    pad = 1

    region = []

    for xx in range(l-pad, r+pad):
        for yy in range(b-pad, t+pad):
            np = complex(xx, yy)
            cp = closest(np)
            grid[np] = cp
            if sum([distance(op-np) for op in points]) < 10_000:
                region.append(np)

    counts = []
    for pnt in points:
        if l < int(pnt.real) < r and b < int(pnt.imag) < t:
            cnt = 0
            for v in grid.values():
                if v == pnt:
                    cnt += 1

            counts.append(cnt)

    return max(counts), len(region)


if __name__ == '__main__':

    lines = pathlib.Path('06.txt').read_text().strip().split('\n')
    print(problem(lines))
