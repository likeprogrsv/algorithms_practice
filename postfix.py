from collections import deque


# Function to evaluate a given postfix expression
def evalPostfix(exp):

	# base case
	if not exp:
		exit(-1)

	# create an empty stack
	stack = deque()

	# traverse the given expression
	for ch in exp:

		# if the current is an operand, push it into the stack
		if ch.isdigit():
			stack.append(int(ch))

		# if the current is an operator
		else:
			# remove the top two elements from the stack
			x = stack.pop()
			y = stack.pop()

			# evaluate the expression 'x op y', and push the
			# result back to the stack
			if ch == '+':
				stack.append(y + x)
			elif ch == '-':
				stack.append(y - x)
			elif ch == '*':
				stack.append(y * x)
			elif ch == '/':
				stack.append(y // x)

	# At this point, the stack is left with only one element, i.e.,
	# expression result
	return stack.pop()


if __name__ == '__main__':

	exp = '1232*+-8-'
	print(evalPostfix(exp))