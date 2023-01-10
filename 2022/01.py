import pathlib

input_string = pathlib.Path('./01.txt').read_text()
lines = input_string.splitlines()

calories = []

for line in lines:
    sm = 0
    if line == "":
        calories.append(sm)
        continue
    sm += int(line)

# part 1
print(max(calories))

# part 2
top_three_sum = sum(sorted(calories, reverse=True)[:3])
print(top_three_sum)