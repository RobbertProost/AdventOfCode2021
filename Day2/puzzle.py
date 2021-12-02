import os
import sys

instructions = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f:
        line = line.split('\n')
        if line:
            instructions.append(line[0])


horizontal = 0
depthA = 0
depthB = 0
aim = 0

for instruction in instructions:
    direction, steps = instruction.split(' ', 1)

    if direction == 'forward':
        horizontal += int(steps)
        depthB += aim * int(steps)
    elif direction == 'down':
        depthA+= int(steps)
        aim += int(steps)
    elif (direction == 'up'):
        depthA -= int (steps)
        aim -= int(steps)
      
print("Result A: ", horizontal * depthA)
print("Result B: ", horizontal * depthB)