import re

f = open("input5.txt", "r")
lines = f.readlines()
coors = {}
for line in lines:
  nums = re.split(r'\D+',line)
  x1 = int(nums[0])
  y1 = int(nums[1])
  x2 = int(nums[2])
  y2 = int(nums[3])
  if x1 == x2:
    for y in range (min(y2,y1),max(y2,y1)+1):
      if (x1,y) in coors:
        coors[(x1,y)] += 1
      else:
        coors[(x1,y)] = 1
  elif y1 == y2:
    for x in range (min(x1,x2),max(x1,x2)+1):
      if (x,y1) in coors:
        coors[(x,y1)] += 1
      else:
        coors[(x,y1)] = 1
  else:
    if y1 > y2:
      dx = x2
      for y in range(y2, y1+1):
        if (dx,y) in coors:
          coors[(dx,y)] += 1
        else:
          coors[(dx,y)] = 1
        if x2 > x1:
          dx -= 1
        else:
          dx += 1
    else:
      dx = x1
      for y in range(y1, y2+1):
        if (dx,y) in coors:
          coors[(dx,y)] += 1
        else:
          coors[(dx,y)] = 1
        if x1 > x2:
          dx -= 1
        else:
          dx += 1

i=0
for coor in coors.items():
  if coor[1] > 1:
    i += 1;

print(i)
