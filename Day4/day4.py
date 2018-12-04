import numpy as np, re

data = [x for x in open("input.txt").readlines()]
data.sort()
records = np.zeros((0, 4), dtype=int)
id = 0

for index, item in enumerate(data):
	h = int(re.search(' (.+?):', item).group(1))
	m = int(re.search(':(.+?)]', item).group(1))
	msg = re.search('] (.+?)$', item).group(1)
	id = re.search('#(.+?) ', item)
	
	if(id): 
		id = int(id.group(1))
		if id in records:
			print id
		else:
			newrow = [[id]]
			records = np.concatenate((records,newrow))
		
		


print(records)