A = 883
B = 879


# A = 65
# B = 8921


def gen_a():
    val = A
    while True:
        val = (16807 * val) % 2147483647
        yield val


def gen_b():
    val = B
    while True:
        val = (48271 * val) % 2147483647
        yield val


def gen_a2():
    val = A
    while True:
        val = (16807 * val) % 2147483647
        if val % 4 == 0:
            yield val


def gen_b2():
    val = B
    while True:
        val = (48271 * val) % 2147483647
        if val % 8 == 0:
            yield val


def part_one():
    n = 0
    a, b = gen_a(), gen_b()
    for i in range(40_000_000):
        if bin(next(a))[-16:] == bin(next(b))[-16:]:
            n += 1

    return n


def part_two():
    n = 0
    a, b = gen_a2(), gen_b2()
    for i in range(5_000_000):
        if bin(next(a))[-16:] == bin(next(b))[-16:]:
            n += 1

    return n


if __name__ == '__main__':
    print(part_one())
    print(part_two())
