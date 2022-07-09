lines = open('input13_ex.txt','r').readlines()
grid = []
folds = []

count = 0
for num, line in enumerate(lines):
    strings = line.strip().split(',')
    if strings[0]: 
        if strings[0][0] != 'f':
            grid.append((strings[0], strings[1]))
        elif strings[0][0] == 'f':
            fold = line.strip().split(' ')[2].split('=')
            folds.append ((fold[0],fold[1]))

print(grid)
print(folds)