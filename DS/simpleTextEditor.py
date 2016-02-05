Q = int(raw_input())
S = ""
stack = []
for i in range(0,Q):
	command = raw_input()
	if int(command[0]) == 1:
		text = command.split()[1]
		S+=text
		stack.append(S)
	elif int(command[0]) == 2:
		index = int(command.split()[1]) * -1
		stack.append(S)
		S=S[:index]
	elif int(command[0]) == 3:
		index = int(command.split()[1])
		print S[index-1]
	else:
		S = stack.pop()
		