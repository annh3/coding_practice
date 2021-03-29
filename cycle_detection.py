

def DFS(cur, g, visited, in_process):
	if cur == None or cur in visited:
		return False

	in_process.add(cur)

	flag = False
	for child in g[cur]:
		if child in in_process:
			return True
		if child not in visited:
			flag = flag or DFS(child, g, visited, in_process)
	in_process.remove(cur)
	visited.add(cur)
	return flag

def DFS_wrapper(cur, g):
	visited = set()
	in_process = set()
	res = False
	for node in g.keys():
		res = res or DFS(node, g, visited, in_process)
	return res

def test1():
	g = {}
	g[0] = [1,2]
	g[1] = [2]
	g[2] = [3,0]
	g[3] = [3]
	visited = set()
	in_process = set()
	res = DFS_wrapper(1, cur)
	#res = DFS(1,g,visited,in_process)
	print("res: ", res)


if __name__ == "__main__":
	test1()
