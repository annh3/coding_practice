

def square_root(k):
	left, right = 0, k
	# Candidate interval [left, right] where everything before left has square
	# <= k, everything after right has square > k
	while left <= right:
		print("Interval Top: [", left, ", ", right, "]")
		mid = (left + right) // 2
		print("Mid: ", mid)
		mid_squared = mid * mid
		if mid_squared <= k:
			left = mid + 1
		else:
			right = mid - 1
		print("Interval Bottom: [", left, ", ", right, "]")
	return left - 1

def test():
	res = square_root(49)
	print("Square root: ", res)

if __name__ == "__main__":
	test()
