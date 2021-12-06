lines = open("input3.txt", "r")
bit_counts = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in lines:
  parts = int(line, 2)
  for x in range(12):
    if (parts & (1 << x)):
      bit_counts[x] += 1

gamma_rate = 0
for x in range(12):
  if bit_counts[x] > 500:
    gamma_rate |= 1 << x

epsilon_rate = ~gamma_rate & 0b111111111111
print(gamma_rate * epsilon_rate)