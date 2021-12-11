from pathlib import Path
import time

with Path(Path(__file__).parent, 'input1.txt').open() as file:
    input = [int(item) for item in file.read().strip().split()]

prev_sum = 0
this_sum = 0
counter = 0
start_index = 0
stop_index = start_index + 3 

while stop_index <= len(input):
    if(prev_sum == 0 and this_sum == 0):
        this_sum = sum(input[start_index:stop_index])
    else:
        this_sum = sum(input[start_index:stop_index])
        if(this_sum > prev_sum):
            counter += 1
    prev_sum = this_sum
    start_index += 1
    stop_index = start_index + 3

print(counter)

