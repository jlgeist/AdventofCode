from string import ascii_lowercase

input = open("input.txt").read().splitlines()[0]

def part1(line):
	x = ''
	while x != line:
		x = line
		for char in ascii_lowercase:
			line = line.replace(char.lower() + char.upper(), '')
			line = line.replace(char.upper() + char.lower(), '')

	return(len(line))

answer1 = part1(input)

test = ''
shortest = len(input)
for char in ascii_lowercase:
	test = input.replace(char, '').replace(char.upper(), '')
	length = part1(test)
	if length < shortest:
		shortest = length;

answer2 = shortest

print(answer1)
print(answer2)
