import numpy as np, re

data = [x for x in open("input.txt").readlines()]
data.sort()
records = np.zeros((1, 62), dtype=int)

for index, item in enumerate(data):
	h = int(re.search(' (.+?):', item).group(1))
	m = int(re.search(':(.+?)]', item).group(1))
	msg = re.search('] (.+?)$', item).group(1)
	hasid = re.search('#(.+?) ', item)
	
	if hasid:
		start = 0
		stop = 0 
		id = int(hasid.group(1))
		if id not in records:
			row = np.zeros((1, 62), dtype=int)
			row[0][0] = id
			records = np.concatenate((records,row))
	if re.search(r'falls', item):	
		if h == 23: 
			m = 0
		start = m
	if re.search(r'wakes', item):	
		stop = m
		for x in range(start, stop):
			k = np.where(records[:,0] == id)[0][0]
			records[k][x+1] += 1
			records[k][61] += 1

c = max(record[61] for record in records)
id1 = records[np.where(records[:,61] == c)[0][0]][0]
r = records[np.where(records[:,61] == c)][0]
r[0] = r[61] = 0
answer1 = (((np.argmax(r))-1) * id1)

b = np.delete(records, (0, 61), axis=1)
ind = np.unravel_index(np.argmax(b, axis=None), b.shape)
answer2 = records[ind[0]][0] * (ind[1])

print answer1
print answer2

