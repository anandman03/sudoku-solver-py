def input_grid(grid: list) -> list:
	"""To fill grid values
	:param grid: 9x9 sudoku board
	:return list: updated sudoku list
	"""
	rows = int(input('Enter number of inputs followed by row,col,val (like 0,0,2)\n'))
	for i in range(rows):
		val = [int(num) for num in input().split(',')]
		grid[val[0]][val[1]] = val[2]
	return grid

def pos_valid(grid: list, dim: list, row: int, col: int, val: int) -> bool:
	"""To check valid position
	:param grid: 9x9 sudoku board
	:param dim: dimension of sudoku board
	:param row: current cell row
	:param col: current cell col
	:param val: value to be checked before injecting
	:return bool: status of move
	"""
	# check number in given row
	for itr in range(dim):
		if grid[row][itr] == val:
			return False

	# check number in given col
	for itr in range(dim):
		if grid[itr][col] == val:
			return False

	# check number in square
	corner_row = (row // 3) * 3
	corner_col = (col // 3) * 3
	for r_itr in range(3):
		for c_itr in range(3):
			if grid[r_itr + corner_row][c_itr + corner_col] == val:
				return False

	return True


def solve_sudoku(grid: list, dim: int, row: int, col: int) -> bool:
	"""To solve the sudoku
	:param grid: 9x9 sudoku board
	:param dim: dimension of sudoku board
	:param row: current cell row
	:param col: current cell col
	:return bool: status of move
	"""

	if col == dim:
		col = 0
		row += 1

	if row == dim:
		return True

	if grid[row][col] > 0:
		return solve_sudoku(grid, dim, row, col+1)

	for val in range(1, 10):
		if pos_valid(grid, dim, row, col, val):
			grid[row][col] = val
			if solve_sudoku(grid, dim, row, col+1):
				return True
			grid[row][col] = 0

	return False

def print_grid(grid: list, dim: int) -> None:
	"""To print the sudoku board
	:param grid: 9x9 sudoku board
	:param dim: dimension of sudoku board
	:return None:
	"""
	for row in range(dim):
		for col in range(dim):
			print(grid[row][col], end=',')
		print('')
	return

def main():
	# data
	dim = 9
	grid = [[0 for j in range(dim)] for i in range(dim)]

	# fill grid from user input
	grid = input_grid(grid)
	# solve sudoku
	if solve_sudoku(grid, dim, 0, 0):
		print_grid(grid, dim)
	else:
		print('No Solution Exist')


if __name__ == '__main__':
	main()
