from pathlib import Path
from collections import Counter

with Path(Path(__file__).parent, 'input3').open() as file:
    input = [line.strip() for line in file.readlines()]

current_column_sums = []

gamma = ['1' if sum(map(int, bit)) > len(input)/2 else '0' for bit in zip(*input)]
epsilon = ['0' if i == '1' else '1' for i in gamma]

def most_common(data: list[str], index: int):
    counts = Counter(x[index] for x in data)
    return '1' if counts['1'] >= counts['0'] else '0'

def least_common(data: list[str], index: int):
    counts = Counter(x[index] for x in data)
    return '0' if counts['0'] <= counts['1'] else '1'

def filter_by(data: list[str], filter_function):
    data = data[:]
    while len(data) > 1:
        for i in range(len(data[0])):
            data = [x for x in data if x[i] == filter_function(data, i)]
            if len(data) == 1:
                break
    return int(''.join(data[0]), 2)

oxy = filter_by(input, most_common)
co2 = filter_by(input, least_common)
print("Part 1: ", int(''.join(gamma), 2) * int(''.join(epsilon), 2))
print("Part 2: ", oxy * co2)
