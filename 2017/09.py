import pathlib


def part_one(chars):
    garbage = False
    current = 0
    total = 0

    i = 0
    while True:
        if i >= len(chars):
            return total
        c = chars[i]
        if garbage:
            if c == '!':
                i += 2
                continue
            elif c == '>':
                garbage = False

        else:
            if c == '{':
                current += 1
                total += current
            elif c == '}':
                current -= 1
            elif c == '<':
                garbage = True
        i += 1


def part_two(chars):
    garbage = False
    total = 0

    i = 0
    while True:
        if i >= len(chars):
            return total
        c = chars[i]
        if garbage:
            if c == '!':
                i += 2
                continue
            elif c == '>':
                garbage = False
            else:
                total += 1

        else:
            if c == '<':
                garbage = True
        i += 1


if __name__ == '__main__':
    chars = pathlib.Path('09.txt').read_text().strip()
    print(part_one(chars))
    print(part_two(chars))
