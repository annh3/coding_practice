import heapq as heapq
import pdb
import networkx as nx
import sys

def read_data(filename):
	f = open(filename, 'r')
	data = f.readlines()
	line1 = data[0]
	n, m = line1.split()
	n = int(n)
	m = int(m)
	data = data[1:]
	G = nx.Graph()

	for line in data:
		l = line.split("\n")[0]
		v, w, cost = l.split()
		#v = int(v)
		#w = int(w)
		cost = int(cost)
		G.add_edge(v,w, weight=cost)

	G = G.to_undirected()
	return G

def prims(G):
	# create T, our MST
	T = nx.Graph()

	# create heap
	nodes = list(G.nodes)
	n = len(nodes)
	V_X = set(nodes)
	#pdb.set_trace()
	X = set()
	v = nodes[0]
	nodes = nodes[1:]

	h = []
	res = list(G.edges(v,data=True))
	res.sort(key=lambda tup: tup[2]['weight'])

	# sort this by weight
	# pdb.set_trace()
	w = res[0][1] # I feel like this is incorrect / come back to later
	#h.append((res[0][2]['weight'],v,w))

	for node in nodes:
		res = list(G.edges(node))
		h.append((sys.maxsize, node, res[0][1])) # choose arbitrary endpoint

	V_X.remove(v)
	X.add(v)
	for v, w in G.edges(v):
		if w in V_X:
			# find and remove w from heap , note w should be (_, w, _)
			loc = -1
			c_prime = sys.maxsize
			v_prime = -1
			w_prime = -1

			for i, tup in enumerate(h):
				if w == tup[1]:
					loc = i
					c_prime = tup[0]
					v_prime = tup[1]
					w_prime = tup[2]
				# delete

			heapsize = len(h)
			tmp = h[0]
			h[loc] = tmp
			heapq.heappop(h)

			c_vw = G[v][w]["weight"]

			# weight update and add
			if c_prime < c_vw:
				heapq.heappush(h, (c_prime, w, w_prime))
			else:
				heapq.heappush(h, (c_vw, w, v))
			assert(len(h) == heapsize)

	heapq.heapify(h)

	"""
	res = G.edges(1)
	print(res)
	[(1, 2), (1, 132), (1, 171), (1, 244), (1, 310), (1, 316), (1, 324), (1, 397), (1, 414)]
	"""

	while len(V_X) > 0:
		# dequeue from heap the shortest edge crossing X, V\X
		# add the node v on its right side to X
		cost, v, w = heapq.heappop(h)

		T.add_edge(v,w,weight=cost)
		V_X.remove(v)
		X.add(v)

		w_star = v

		# for each edge (v,w) \in E, if w in V\X
		for v, w in G.edges(w_star):
			#pdb.set_trace()
			if w in V_X: # it MUST be in the heap 
				# find and remove w from heap , note w should be (_, w, _)
				loc = -1
				c_prime = sys.maxsize
				v_prime = -1
				w_prime = -1

				for i, tup in enumerate(h):
					#pdb.set_trace()
					if w == tup[1]:
						loc = i
						c_prime = tup[0]
						v_prime = tup[1]
						w_prime = tup[2]
				# delete
				assert(loc != -1)
				#pdb.set_trace()
				heapsize = len(h)
				tmp = h[0]
				h[loc] = tmp
				heapq.heappop(h)

				c_vw = G[v][w]["weight"]

				# weight update and add
				if c_prime < c_vw:
					heapq.heappush(h, (c_prime, w, w_prime))
				else:
					heapq.heappush(h, (c_vw, w, v))
				assert(len(h) == heapsize)
	return T

if __name__ == "__main__":
	G = read_data('prims_data_small.txt')
	T = prims(G)
