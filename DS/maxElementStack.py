N = int(raw_input())
stack = []
current_max = 0
for i in range(0,N):
	a = raw_input()
	if " " in a:
		query_type,x = map(int, a.split())
		stack.append(x)
		if current_max < x:
			current_max = x
	else:
		query_type = int(a)
		if query_type == 2:
			stack.pop()
			current_max=max(stack)
		if query_type == 3:
			print current_max
