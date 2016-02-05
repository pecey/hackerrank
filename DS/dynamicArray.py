def calcSequence(x, lastans, N):
	return ((x^lastans)%N);

N,Q = map(int, raw_input().split())

arr = []
lastans = 0
for i in xrange(N):
	arr.append([])

for i in range(0,Q):
	a,b,c = map(int, raw_input().split())
	if a == 1:
		index = calcSequence(b, lastans, N)
		arr[index].append(c)
	if a == 2:
		index = calcSequence(b, lastans, N)
		size = len(arr[index])
		lastans = arr[index][c%size]
		print lastans