import heapq



def bfs(s):
	graph = {
	1: [2],
	2: [3,4],
	3: [4],
	4: [5],
	5: [],
	}

	# print("graph: ", graph[2])

	# just process the nodes one by one
	visited = set()
	queue = [s]
	visited.add(s)
	
	while len(queue) > 0:
		cur = queue.pop(0)
		print(cur)
		#print("graph of cur: ", graph[cur])

		for child in graph[cur]:
			print("child: ", child, " of parent: ", s)
			if child not in visited:
				queue.append(child)
				#print("added child: ", child)
				#print("queue: ", queue)
				visited.add(child)
		#print("length of queue: ", len(queue))

bfs(1)

