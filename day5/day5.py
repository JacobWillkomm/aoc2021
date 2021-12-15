from pathlib import Path

with Path(Path(__file__).parent, 'input5').open() as file:
    input = [line.strip() for line in file.readlines()]

line_positions = {}

for line in input:
    first_coord = line.split()[0].split(',')
    second_coord = line.split()[2].split(',')
    x_slope = int(second_coord[0]) - int(first_coord[0])  
    y_slope = int(second_coord[1]) - int(first_coord[1]) 
    if(x_slope == 0):
        for y in range(min(int(first_coord[1]), int(second_coord[1])), max(int(first_coord[1]), int(second_coord[1]))+1):
            if(int(first_coord[0]), y) not in line_positions:
                line_positions[(int(first_coord[0]), y)] = 1
            else:
                line_positions[(int(first_coord[0]), y)] += 1

    elif(y_slope == 0):
        for x in range(min(int(first_coord[0]), int(second_coord[0])), max(int(first_coord[0]), int(second_coord[0]))+1):
            if(x, int(first_coord[1])) not in line_positions:
                line_positions[(x, int(first_coord[1]))] = 1
            else:
                line_positions[(x, int(first_coord[1]))] += 1

    else:
        current_x_pos = int(first_coord[0])
        current_y_pos = int(first_coord[1])
        for i in range(0, abs(x_slope)+1): #This only works because the slope of the line will always be 1 or -1
            if(current_x_pos, current_y_pos) not in line_positions:
                line_positions[(current_x_pos, current_y_pos)] = 1
            else:
                line_positions[(current_x_pos, current_y_pos)] += 1
            if x_slope < 0:
                current_x_pos -= 1
            else:
                current_x_pos += 1
            if y_slope < 0:
                current_y_pos -= 1
            else:
                current_y_pos += 1

num_intersections = 0
for key in line_positions:
    if(line_positions[key] > 1):
        num_intersections += 1

print(num_intersections)
