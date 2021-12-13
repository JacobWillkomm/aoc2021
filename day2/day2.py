from pathlib import Path

with Path(Path(__file__).parent, 'input2').open() as file:
    input = [line for line in file.read().strip().split('\n')]

direction_sums = {}
aim = 0
current_depth = 0
current_distance = 0
for line in input:
    if(line.split(' ')[0] == "down"):
        aim += int(line.split(' ')[1])
    elif(line.split(' ')[0] == "up"):
        aim -= int(line.split(' ')[1])
    else: #forward
        current_depth += aim * int(line.split(' ')[1])
        current_distance += int(line.split(' ')[1])

    if(line.split(' ')[0] in direction_sums):
        direction_sums[line.split(' ')[0]] += int(line.split(' ')[1])
    else:
        direction_sums[line.split(' ')[0]] = int(line.split(' ')[1])

print(direction_sums["forward"], current_distance)
print("Part 1: ",(direction_sums["down"] - direction_sums["up"]) * direction_sums["forward"])
print("Part 2: ",(current_depth * current_distance))
