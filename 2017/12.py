import pathlib


def parse_line(ln):
    a, b = ln.split(' <-> ')
    return int(a), set(map(int, map(str.strip, b.split(','))))


def merge(G):
    for i in G:
        for j in list(G[i]):
            if G[j] == G[i]:
                continue
            G[i].update(G[j])
            G[j] = G[i]

    return G


def part_one(lines):
    mapping = {}
    for line in lines:
        k, v = parse_line(line)
        mapping[k] = v
    merged = merge(mapping)
    return len(merged[0])


def part_two(lines):
    mapping = {}
    for line in lines:
        k, v = parse_line(line)
        mapping[k] = v

    merged = merge(mapping)
    reprs = set()

    for s in merged.values():
        rpr = ''.join(str(sorted(s)))
        reprs.add(rpr)

    return len(reprs)


if __name__ == '__main__':

    lines = pathlib.Path('12.txt').read_text().strip().split('\n')
    print(part_one(lines))
    print(part_two(lines))
