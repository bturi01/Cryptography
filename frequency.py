import collections

d = collections.defaultdict(int)

ciphertext = open('text.txt')
for line in ciphertext:
	line = line.rstrip('/n')
	for c in line:
		d[c] += 1

print d #defaultdict(<type 'int'>, {'s': 1, 'e': 1, 't': 2})
