lines = open("input2.txt", "r")
x = 0
z = 0
aim = 0
for line in lines:
  parts = line.split(' ')
  direction = parts[0]
  val = int(parts[1])
  if (direction == 'forward'):
    x += val
    z += (val * aim) 
  elif (direction == 'down'):
    aim += val
  elif (direction == 'up'):
    aim -= val
print("Answer is: " + str(x*z))
