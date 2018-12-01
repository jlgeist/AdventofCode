import itertools

data = [int(x) for x in open("input.txt").readlines()]

answer1 = (sum(data))

frequency = 0
seen = set([0])
for val in itertools.cycle(data):
	frequency += val
	if frequency in seen:
		answer2 = frequency
		break
	seen.add(frequency)

print(answer1)
print(answer2)
