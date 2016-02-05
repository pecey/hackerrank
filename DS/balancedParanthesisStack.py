N = int(raw_input())
for i in range(0,N):
	temp = raw_input()
	stack = []
	flag = True
	for i in range(0, len(temp)):
		if temp[i] == '{' or temp[i] == '[' or temp[i] == '(':
			stack.append(temp[i])
		elif len(stack)==0:
			flag=False
			break
		else:
			head = len(stack)-1
			if temp[i] == '}' and stack[head] == '{':
				stack.pop()
			elif temp[i] == ']' and stack[head] == '[':
				stack.pop()
			elif temp[i] == ')' and stack[head] == '(':
				stack.pop()
			else:
				flag = False
				break
	if len(stack) or not flag:
		print "NO"
	else:
		print "YES"