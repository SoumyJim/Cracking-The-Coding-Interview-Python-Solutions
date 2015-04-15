__author__ = 'Jim'

def demo(matrix):
	M = len(matrix)
	if M == 0:
		return matrix
	N = len(matrix[0])
	row_flag = 0
	col_flag = 0
	for i in range(M):
		for j in range(N):
			if matrix[i][j] == 0:
				row_flag |= (1 << i)
				col_flag |= (1 << j)


	for i in range(M):
		for j in range(N):
			if (matrix[i][j] != 0):
				if (row_flag & (1 << i)) or (col_flag & (1 << j)):
					matrix[i][j] = 0
	return matrix

print(demo([[1,0,3], [4,5,0], [7,8,9]]))