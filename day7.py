import re
import statistics

f = open("input7.txt",'r')
lines = f.readlines()

crab_pos = []
for line in lines:
    for i in line.split(','):
        crab_pos.append(int(i))


def fuel_calc (d):
    val = 0
    for i in range(0,d+1):
        val += i 
    return val

min_f = fuel_calc(len(crab_pos)) * max(crab_pos)

for point in range(min(crab_pos), max(crab_pos)+1):
    f = 0
    for pos in crab_pos:
        f += fuel_calc(abs(pos - point))
    if f < min_f:
        min_f = f

print(min_f)
        