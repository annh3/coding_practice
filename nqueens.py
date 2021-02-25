#annhe

# input is n, the size of the board and the number of queens
# output is res, a list of lists
# each list is length n and the ith entry represents the column that
# the queen in the ith row is placed in

# the recursive strucutre of the code is
# we are placing the nth queen 
# we are placing the (n-1)th queen
# we are placing the (n-2)th queen
# ...
# down to placing the 1st queen, the base case
# in the base case, we have only one option for column left, 
# but i don't know if we have to check yet

# in each iteration to place the k^th queen
# we have to check that it doesn't invalidate the (n-k) placed
# before
# it cannot be in the same row, column, or diagonal
# i, a[i] is the row, col of the ith queen, then
# we cannot have abs(i-cur_row) == abs(a[i]-cur_col)
# this handles diagonals
# does this also handle row, col?
# row is already handled by the recursive structure of the problem
# col is handled by... we can do an extra check a[i] != cur_col

# what datastructures?
# we pass along an array of the current answer, this is copied on recursion

import copy

def nqueens(n):
	res = []
	a = [0]*n

	def place_queens(n,k, a):
		if k == n:
			res.append(a)
			return

		# we are placing the kth queen
		# we've used a[0] through a[n-k-1]
		for cur_col in range(n):
			if all(abs(k-row) != abs(cur_col-col) and col != cur_col
				for row, col in enumerate(a[:k])
				):
				a_copy = copy.deepcopy(a)
				a_copy[k] = cur_col
				place_queens(n,k+1,a_copy)

	place_queens(n,0,a)
	return res

if __name__ == "__main__":
	result = nqueens(4)
	print(result)