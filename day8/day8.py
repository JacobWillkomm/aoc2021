from pathlib import Path
from collections import Counter

with Path(Path(__file__).parent, 'input8').open() as file:
    input = [line.strip() for line in file.readlines()]

class Display:
    def __init__(self, display):
        self.key = {}
        self.display = self.get_display(display)

    def get_display(self, display):
        display_key = {}
        key_data = display.split('|')[0].strip()
        display_data = display.split('|')[1].strip()
        queue = []
        for k_data in key_data.split(' '): #add unique indecies to the key, and otherwise add them to the queue
            key_set = set(k_data)
            if len(key_set) == 2:
                display_key[1] = key_set
            elif len(key_set) == 3:
                display_key[7] = key_set
            elif len(key_set) == 4:
                display_key[4] = key_set
            elif len(key_set) == 7:
                display_key[8] = key_set
            else:
                queue.append(key_set)
                #rest of the numbers
        while len(queue) > 0: #while the queue is not empty
            if len(queue[0]) == 5:
                #2, 3, 5 are possible
                if display_key[1].issubset(queue[0]):
                    display_key[3] = queue.pop(0)
                elif (display_key[4]^display_key[1]).issubset(queue[0]):
                    display_key[5] = queue.pop(0)
                else:
                    display_key[2] = queue.pop(0)

            elif len(queue[0]) == 6:
                #0, 6, 9 are possible
                if(2 in display_key and 3 in display_key and 5 in display_key): #2, 3 and 5 are used to decipher 6 and 9 
                    if (display_key[2]^display_key[3]).union(display_key[5]) == queue[0]:
                        display_key[6] = queue.pop(0)
                    elif display_key[1].union(display_key[5]) == queue[0]:
                        display_key[9] = queue.pop(0)
                    else:
                        display_key[0] = queue.pop(0)
                else: #if 2, 3 or 5 are not already in the key, re-add them to the queue
                    queue.append(queue.pop(0))
            
        self.key = display_key
        
        key_list = list(display_key.keys())
        val_list = list(display_key.values())
        display_text = ''
        for display_number in display_data.split(' '):
            display_text += (str(key_list[val_list.index(set(display_number))]))

        return display_text

d = Display(input[0])
print(d.display)
display_list = []
c = Counter()
total = 0
for d in input:
    this_display = Display(d)
    c.update(this_display.display)
    total += int(this_display.display)
print(c)
print(total)
