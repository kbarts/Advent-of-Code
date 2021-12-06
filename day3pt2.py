def process_vals(vals, i, mc):
  if len(vals) == 1:
    return vals[0]
  vals.sort()     
  new_vals = []
  for j, val in enumerate(vals):
    if (val & (1 << i)):
      if mc:
        if (j > len(vals)/2):
          new_vals = vals[0:j]
        else:
          new_vals = vals[j:len(vals)]
      else:
        if (j > len(vals)/2):
          new_vals = vals[j:len(vals)]
        else:
          new_vals = vals[0:j] 
      break
    elif (j == len(vals) - 1):
      if mc:
        new_vals = vals
  return process_vals(new_vals, i - 1, mc)

lines = open("input3.txt", "r")
vals = []
for line in lines:
  vals.append(int(line, 2))
vals.sort()
oxy = 0
co2 = 0

for i, val in enumerate(vals):
  if (val & (1 << 11)):
    if i > len(vals) / 2:
      oxy = process_vals(vals[0:i],10,True)
      co2 = process_vals(vals[i:len(vals)],10,False) 
    else:
      oxy = process_vals(vals[i:len(vals)],10,True) 
      co2 = process_vals(vals[0:i],10,False)
    break
      
print(oxy * co2)