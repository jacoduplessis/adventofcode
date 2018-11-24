import sys
import os
import pathlib
from urllib.request import urlopen, Request

year = sys.argv[1]
days = sys.argv[2:]


if not all([year, days]):
    print("Invalid input. Usage: python3 get_input.py <YEAR> <DAYS>")
    sys.exit(1)

os.makedirs(year, exist_ok=True)
session = pathlib.Path('session.txt').read_text()

for day in days:

    req = Request(f'https://adventofcode.com/{year}/day/{day}/input', headers={
        'Cookie':f'session={session}'
    })

    resp = urlopen(req).read()

    to = str(day).zfill(2)

    with open(os.path.join(year, f'{to}.txt'), 'wb') as out:
        out.write(resp)

