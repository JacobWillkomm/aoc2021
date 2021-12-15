from pathlib import Path
from statistics import mean, median

with Path(Path(__file__).parent, 'input7').open() as file:
    input = [int(line) for line in file.read().strip().split(',')]

part2_target_position = round(mean(input))
part2_fuel_cost = 0
for current_position in input:
    dis = abs(current_position - part2_target_position)
    part2_fuel_cost += (1/2)*dis*(dis+1) 

print("Part2: ", part2_fuel_cost)


crab_positions = sorted(input)
part1_target_position = median(input)
part1_fuel_cost = 0

for current_position in input:
    part1_fuel_cost += abs(current_position - part1_target_position)

print("Part1: ", part1_fuel_cost)
