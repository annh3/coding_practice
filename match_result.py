import collections
import queue

MatchResult = collections.namedtuple('MatchResult', ('winning_team', 'losing_team'))

def alternative_bfs(graph, curr, dest):
	if curr == dest:
		return True

	q = queue.Queue()
	visited = set()
	q.put(curr)

	while not q.empty():
		curr = q.get()
		if curr == dest:
			return True
		for team in graph[curr]:
			if team not in visited:
				visited.add(team)
				q.put(team)

	return False

def can_team_a_beat_team_b(matches, team_a, team_b):
	def build_graph():
		graph = collections.defaultdict(set)

		for match in matches:
			graph[match.winning_team].add(match.losing_team)
		return graph

	def is_reachable_dfs(graph, curr, dest, visited = set()):
		if curr == dest:
			return True
		elif curr in visited or curr not in graph:
			return False # we return false because we don't want to visit infinitely
			# there should be a more efficient way to do this # let's run a test
		visited.add(curr)

		return any(is_reachable_dfs(graph, team, dest)
			for team in graph[curr])

	graph = build_graph()
	#return is_reachable_dfs(graph, team_a, team_b)
	return alternative_bfs(graph, team_a, team_b)

if __name__ == "__main__":
	match1 = MatchResult('A', 'B') # do they give an example in the book?
	match2 = MatchResult('C', 'D')
	match3 = MatchResult('B', 'E')
	match4 = MatchResult('D', 'E')
	match5 = MatchResult('E', 'F')
	match6 = MatchResult('F', 'G')
	match7 = MatchResult('E', 'H')
	match8 = MatchResult('F', 'I')
	match9 = MatchResult('I', 'M')
	match10 = MatchResult('I', 'J')
	match11 = MatchResult('M', 'K')
	match12 = MatchResult('K', 'L')

	matches = [match1, match2, match3, match4, match5, match6, 
		match7, match8, match9, match10, match11, match12]

	res = can_team_a_beat_team_b(matches, 'A', 'L')

	print("result: ", res)