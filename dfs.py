import copy

class Node:
	def __init__(self, name=-1, children=[]):
		self.color = "white"
		self.parent = None
		self.d = 0
		self.f = 0
		self.name = name
		self.children = children

time = 0

def dfs_visit(cur, sorted_list):
	print("apples")
	global time
	time += 1
	cur.d = time
	cur.color = "gray"
	print("hello")
	for child in cur.children:
		if child.color == "white":
			child.parent = cur
			dfs_visit(child, sorted_list)
	cur.color = "black"
	time += 1
	cur.f = time
	sorted_list.append(cur.name)

def dfs(root):
	sorted_list = []
	print("bananas")
	dfs_visit(root, sorted_list)
	return sorted_list


def test():
	node5 = Node(5)
	node4 = Node(4,[node5])
	node3 = Node(3,[node4])
	node2 = Node(2,[node3,node4])
	node1 = Node(1,[node2])
	print("oranges")
	topo = dfs(node1)
	for t in topo:
		print("t: ", t)


if __name__ == "__main__":
	test()
