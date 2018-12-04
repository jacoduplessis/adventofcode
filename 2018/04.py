import collections
import pathlib
import re
import datetime


def problem(input_):
    entries = []
    for line in input_:
        ts, action = re.match(r'\[(.*?)\] (.*)', line).groups()
        dt = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M')
        wake = 'wakes up' in action
        sleep = 'sleep' in action
        gid = None
        if 'Guard' in action:
            gid = action.split(' ')[1].strip('#')
        entries.append({
            'date': dt,
            'wake': wake,
            'sleep': sleep,
            'gid': gid,
        })

    cgid = None
    entries = sorted(entries, key=lambda x: x['date'])
    guards = collections.defaultdict(lambda: collections.defaultdict(int))
    for ix, entry in enumerate(entries):
        if (entry['wake'] or entry['sleep']) and not cgid:
            continue
        if entry['gid']:
            cgid = entry['gid']
            continue
        if entry['wake']:
            continue
        if entry['sleep']:
            delta = entries[ix + 1]['date'] - entry['date']
            current_minute = entry['date'].minute
            delta_minutes = int(delta.seconds / 60)
            for i in range(delta_minutes):
                minute_id = (current_minute + i) % 60
                guards[cgid][minute_id] += 1

    highest_total = 0
    highest_id = None

    guard_max_counts = collections.defaultdict(int)
    guard_max_minute = collections.defaultdict(int)

    for gid, minute_dict in guards.items():
        total = sum(minute_dict.values())
        if total >= highest_total:
            highest_id = gid
            highest_total = total
        for minute, count in minute_dict.items():
            if count > guard_max_counts[gid]:
                guard_max_counts[gid] = count
                guard_max_minute[gid] = minute

    highest_minute_id = None
    highest_minute_count = 0
    for mid, cnt in guards[highest_id].items():
        if cnt > highest_minute_count:
            highest_minute_count = cnt
            highest_minute_id = mid

    uber_max_id = None
    uber_max_count = 0
    for gid, count in guard_max_counts.items():
        if count > uber_max_count:
            uber_max_id = gid
            uber_max_count = count

    return int(highest_minute_id) * int(highest_id), int(uber_max_id) * int(guard_max_minute[uber_max_id])


if __name__ == '__main__':
    lines = pathlib.Path('04.txt').read_text().strip().split('\n')
    print(problem(lines))
