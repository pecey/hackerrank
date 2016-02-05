N = int(raw_input())
arr = {}
for i in range(0,N):
	tmp = raw_input()
	if tmp in arr.keys():
		arr[tmp]=arr[tmp]+1
	else:
		arr[tmp]=1

Q = int(raw_input())
for i in range(0,Q):
	tmp = raw_input()
	if tmp in arr.keys():
		print arr[tmp]
	else:
		print 0