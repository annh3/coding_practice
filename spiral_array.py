# ann he

def compute_spiral(arr):
	if len(arr) == 0:
		return []
	n = len(arr[0])
	if n == 1:
		return [arr[0][0]]

	cur = []
	for i in range(n):
		cur.append(arr[0][i])
	for i in range(1,n):
		cur.append(arr[i][n-1])
	for i in range(1,n):
		cur.append(arr[n-1][n-1-i])
	for i in range(1,n-1):
		cur.append(arr[n-1-i][0])

	return cur + compute_spiral(arr[1:n-1][1:n-1])

def test1():
	arr = [[1,2,3],[4,5,6],[7,8,9]]
	res = compute_spiral(arr)
	print(res)

if __name__ == "__main__":
	test1()
