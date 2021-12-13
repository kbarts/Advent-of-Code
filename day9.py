lines = open('input9.txt','r').readlines()
vals = []
for num, line in enumerate(lines):
    vals.append([])
    for i in line.strip():
        vals[num].append(int(i))

for row in vals:
    for val in row:
    