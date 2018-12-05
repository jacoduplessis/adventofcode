import pathlib


def must_react(c, nc):
    return c.lower() == nc.lower() and ((c.islower() and nc.isupper()) or (c.isupper() and nc.islower()))


def problem(input_):
    while True:
        num_reactions = 0

        for ix in range(len(input_)):
            try:
                c = input_[ix]
                nc = input_[ix + 1]
            except IndexError:
                break
            if must_react(c, nc):
                input_ = input_[:ix] + input_[ix + 2:]
                num_reactions += 1

        if num_reactions == 0:
            break

    return len(input_), None


def part_two(input_: str):
    fewest = 99999999

    for a in 'abcdefghijklmnopqrstuvwxyz':
        A = a.upper()
        i = input_.replace(a, '').replace(A, '')
        if len(i) == len(input_):
            continue
        while True:
            num_reactions = 0
            for ix in range(len(i)):
                try:
                    c = i[ix]
                    nc = i[ix + 1]
                except IndexError:
                    break
                if must_react(c, nc):
                    i = i[:ix] + i[ix + 2:]
                    num_reactions += 1

            if num_reactions == 0:
                break

        if len(i) <= fewest:
            fewest = len(i)

    return fewest


if __name__ == '__main__':
    lines = pathlib.Path('05.txt').read_text().strip()
    print(problem(lines))
    print(part_two(lines))

