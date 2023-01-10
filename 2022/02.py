import pathlib

input_string = pathlib.Path('./02.txt').read_text()
lines = input_string.splitlines()

"""
A X - Rock Lose
B Y - Paper Draw
C Z - Scissors Win
"""

points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3,
}

score = 0
score2 = 0

for line in lines:
    op, pl = line.split(' ')
    score += points[pl]

    # draw
    if pl == 'Y':
        score2 += 3
        score2 += points[op]

    # win
    if pl == 'Z':
        score2 += 6
        if op == 'A':
            score2 += points['Y']
        elif op == 'B':
            score2 += points['Z']
        elif op == 'C':
            score2 += points['X']

    # lose
    if pl == 'X':
        if op == 'A':
            score2 += points['Z']
        elif op == 'B':
            score2 += points['X']
        elif op == 'C':
            score2 += points['Y']


    if points[op] == points[pl]:
        score += 3

    elif op == 'A':
        if pl == 'Y':
            score += 6
            continue
    elif op == 'B':
        if pl == 'Z':
            score += 6
            continue
    elif op == 'C':
        if pl == 'X':
            score += 6
            continue

print(score)
print(score2)

