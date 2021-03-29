# Kahn's algorithm for topological sort

def topo_sort(g): # a dictionary adjacency list

	# pre-processing step 1
	incoming_count = {a: 0 for a in g.keys()}
	for a in g.keys():
		for b in g[a]:
			incoming_count[b] += 1

	q = []
	for a in incoming_count.keys():
		if incoming_count[a] == 0:
			q.append(a)

	sort = []
	while len(q) > 0:
		cur = q.pop(0)
		sort.append(cur)
		# decrease
		for child in g[cur]:
			incoming_count[child] -= 1
			if incoming_count[child] <= 0:
				q.append(child)

	return sort

def test1():
	g = {'e': ['r'], 'f': [], 'r': ['t'], 't': ['f'], 'w': ['e']}
	res = topo_sort(g)
	print(res)

if __name__ == "__main__":
	test1()
