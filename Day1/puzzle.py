import os
import sys
import numpy

depths = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f:
        line = line.split()
        if line:
            depths.append(int(line[0]))


resultA = 0
resultB = 0

for i, depth in enumerate(depths):
    if (i > 0):
        resultA += 1 if (depth - depths[i-1] > 0) else 0

depths3 = numpy.lib.stride_tricks.sliding_window_view(depths, 3)
for i, depth in enumerate(depths3):
    if (i > 0):
        resultB += 1 if (sum(depth) - sum(depths3[i-1]) > 0) else 0
        

print("Result A: ", resultA)
print("Result B: ", resultB)