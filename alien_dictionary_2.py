



def alien_dictionary(words):

	# Here's how you do a double for loop list comprehension
	reverse_adj_list = {c: [] for word in words for c in word}

	# add edges to the adjacency list

	"""
	I think the structure that you need to understand here is that information is only useful up to the “first difference”
	That’s what alphabetical order means
	Same as numeric order right?
	Because we have a total ordering on symbols
	"""

	for word1, word2 in zip(words, words[1:]):
		for c1, c2 in zip(word1, word2):
			if c1 != c2: # then c2 --> c1 in our graph
				reverse_adj_list[c2].append(c1)
				break

	# DFS
	output = []
	seen = {} # False = gray, True = black

	# Defining this function internally
	"""
	Note that if the graph has cycles, then the alphabet is invalid
	"""

	"""
	Graph Coloring

	In directed graphs, we often detect cycles by using graph coloring
	All nodes start out as white 
	Once they're visited they become grey
	Once all of their outgoign nodes have been fully explored, they become black

	We know there is a cycle if we enter a node that is currently grey
	All nodes that are currently on the stack are grey
	Nodes are changed to balck when they are removed from the stack
	"""

	def visit(node): # we don't need to return anything
		if node in seen:
			return seen[node] # return this color, if this

		node[seen] = False # this is grey

		for c in reverse_adj_list[node]:
			result = visit(c) # get rid of our check, so that we can detect cycle
			if not result: # node is grey
				return False # cycle

		seen[node] = True # we managed to visit without a cycle
		output.append(node)
		return True

	if not all(visit(node) for node in reverse_adj_list):
		return ""
	else:
		return "".join(output)






if __name__ == "__main__":
	test()
