import requests
import sys
import os

year = sys.argv[1]
days = sys.argv[2:]


if not all([year, days]):
    print("Invalid input. Usage: python3 get_input.py <YEAR> <DAYS>")
    sys.exit(1)

d = f'{year}/input'
os.makedirs(d, exist_ok=True)
with open('session.txt', 'r') as session_file:
    session = session_file.read()

s = requests.Session()

for day in days:
    input_string = s.get(
        f'https://adventofcode.com/{year}/day/{day}/input',
        cookies=dict(session=session)
    ).text

    with open(os.path.join(d, f'{day}.txt'), 'w') as out:
        out.write(input_string)

