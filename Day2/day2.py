from collections import Counter

count2 = 0
count3 = 0
with open('input.txt', 'r') as lines:  
    for line in lines:
        chars = Counter(line)
        if 2 in chars.values():
        	count2+=1
        if 3 in chars.values():
        	count3+=1

answer1 = count2 * count3

def removeChar(str, n):
	sub1 = str[:n] 
	sub2 = str[n+1:]
	return sub1 + sub2

data = [x for x in open("input.txt").readlines()]
length = len(data)
for index, item in enumerate(data):
	string1 = item
	for x in range(0, length-1):
		string2 = data[x]
		matchString = string2
		for i, c in enumerate(string1):
			if c != string2[i]:
				matchString = removeChar(matchString, i)
		if len(matchString) == len(string1)-1:
			answer2 = matchString
			break

print(answer1)
print(answer2)