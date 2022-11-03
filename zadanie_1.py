import sys


def main(n):
	size = (2*n + 1)
	# matrix = [0] * size
	negative = 0
	positive = 0
	for row in range(0, size):
		col_matrix = [0] * size
		for column in range(0, size):
			if column == row:
				col_matrix[column] = 0
				continue
			if row % 2 == 0:
				if column % 2 != 0 and column != row:
					positive += 1
					col_matrix[column] = positive
				else:
					negative = ((((size-1) * (column+1))  + row) // 2) * (-1)
					col_matrix[column] = negative
			else:
				if column % 2 != 0 and column != row:
					negative = ((((size-1) * (column +1)) + row) // 2) * (-1)
					col_matrix[column] = negative
				else:
					# negative = ((size * column) + (row + 1)) % 2
					positive += 1
					col_matrix[column] = positive

		print(*col_matrix, sep=' ')

	pass


if __name__ == '__main__':
	main(int(sys.stdin.readline()))