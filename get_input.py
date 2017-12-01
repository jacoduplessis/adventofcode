import requests
import sys
import os

YEAR = sys.argv[1]
DAY = sys.argv[2]

if not all([YEAR, DAY]):
    sys.exit(1)

input_string = requests.get(
    f'https://adventofcode.com/{YEAR}/day/{DAY}/input',
    cookies=dict(session=open('session.txt', 'r').read())
).text

d = f'{YEAR}/input'
os.makedirs(d, exist_ok=True)
with open(os.path.join(d, f'{DAY}.txt'), 'w') as out:
    out.write(input_string)

