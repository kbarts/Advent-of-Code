lines = open('input10.txt','r').readlines()

def is_an_end(x):
    if x == ')' or x == '}' or x == ']' or x == '>':
        return True

def opposite_off(x):
    if x == '(':
        return ')'
    elif x == ')':
        return '('
    elif x == '{':
        return '}'
    elif x == '}':
        return '{'
    elif x == '[':
        return ']'
    elif x == ']':
        return '['
    elif x == '<':
        return '>'   
    elif x == '>':
        return '<'   

def num_points(x):
    if x == '(':
        return 1
    elif x == '{':
        return 3
    elif x == '[':
        return 2  
    elif x == '<':
        return 4  

sum = 0
scores = []
for num, line in enumerate(lines):
    stack = []
    error = 0
    score = 0
    for l in line.strip():
        if is_an_end(l):
            if stack[-1] == opposite_off(l):
                stack.pop()
            else:
                error = 1
                break
        else:
            stack.append(l)
    if stack and not error:
        while stack:
            score = score * 5 + num_points(stack.pop())
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])

    



            