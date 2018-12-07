import collections
import pathlib


def problem(lines):
    graph = collections.defaultdict(set)
    all_steps = set()
    for line in lines:
        words = line.split(' ')
        req, step = words[1], words[7]
        all_steps.add(req)
        all_steps.add(step)
        graph[step].add(req)

    N = len(all_steps)
    completed = []

    workers = {}
    for i in range(5):
        workers[i] = 0

    def available_tasks():
        available = []
        for s in all_steps:
            r = graph[s]
            if r.issubset(set(completed)) and s not in completed:
                available.append(s)
        return sorted(available)

    seconds = 0
    backlog = {}

    while len(completed) < N:

        for step in available_tasks():
            if step not in backlog:
                for wid, time in workers.items():
                    if time > 0:
                        continue
                    duration = ord(step) - 4
                    workers[wid] = duration
                    backlog[step] = duration
                    break

        for wid in workers:
            if workers[wid] > 0:
                workers[wid] = workers[wid] - 1

        for item in backlog:
            backlog[item] -= 1
            if backlog[item] == 0:
                completed.append(item)

        seconds += 1

    return "".join(completed), seconds


if __name__ == '__main__':
    lines = pathlib.Path('07.txt').read_text().strip().split('\n')
    print(problem(lines))
