import re, numpy as np

fabric = np.empty((1000, 1000))
answer1 = 0
answer2 = 0
safe = 0

with open('input.txt', 'r') as lines:  
    for line in lines:
        i = int(re.search('#(.*) @', line).group(1))
        x = int(re.search('@ (.*),', line).group(1))
        y = int(re.search(',(.*):', line).group(1))
        w = int(re.search(': (.*)x', line).group(1))
        h = int(re.search('x(.*)', line).group(1))

        for a in range(x, x+w):
            for b in range(y, y+h):
                if fabric[a][b] > 0:
                    fabric[a][b] = -1
                    answer1+=1
                elif fabric[a][b] == 0:
                    fabric[a][b] = i

with open('input.txt', 'r') as lines:  
    for line in lines:
        safe = 1
        i = int(re.search('#(.*) @', line).group(1))
        x = int(re.search('@ (.*),', line).group(1))
        y = int(re.search(',(.*):', line).group(1))
        w = int(re.search(': (.*)x', line).group(1))
        h = int(re.search('x(.*)', line).group(1))

        for a in range(x, x+w):
            for b in range(y, y+h):
                if fabric[a][b] != i:
                    safe-=1
                    break

        if safe == 1:
            answer2 = i
            break

print(answer2)

