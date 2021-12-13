#6 -> 0 or 6 or 9
#5 -> 2 or 3 or 5

 # the five digit number that contains the two digit number is a 3
 # the five digit number that contains one less than the 6 is the 5

 # the six digit number that conatins the 4 digit number is the 9
 # the six digit number that does not contain the 2 digit number is the 6
 # process of elimination for last 6 digit number

from os import NGROUPS_MAX


f = open('input8.txt', 'r')
lines = f.readlines()
sum = 0

for num, line in enumerate(lines):
    codes = []
    outputs = []
    solutions = [set() for i in range(0,10)]
    fives = []
    sixes = []
   
    for i in line.strip().split(' | ')[0].split(' '):
        letters = set()
        for l in i:
            letters.add(l)
        codes.append(letters)
    for code in codes:
        if len(code) == 2:
            solutions[1] = code
        if len(code) == 3:
            solutions[7] = code
        if len(code) == 4:
            solutions[4] = code
        if len(code) == 5:
            fives.append(code)
        if len(code) == 6:
            sixes.append(code)
        if len(code) == 7:
            solutions[8] = code

    for six in sixes:
        if solutions[4].issubset(six):
            solutions[9] = six
        elif not solutions[1].issubset(six):
            solutions[6] = six
        else:
            solutions[0] = six
    
    for five in fives:
        if solutions[1].issubset(five):
            solutions[3] = five
        elif five.issubset(solutions[6]):
            solutions[5] = five
        else:
            solutions[2] = five

    for i in line.strip().split(' | ')[1].split(' '):
        letters = set()
        for l in i:
            letters.add(l)
        outputs.append(letters)

    local_sum = 0
    for idx, output in enumerate(outputs):
        for num, i in enumerate(solutions):
            if i == output:
                local_sum += (num * pow(10,3-idx))
    sum += local_sum

print(sum)