class Solution:
    def index_diff(self, str1, str2):
        index = next((i for i, (char1, char2) in enumerate(zip(str1, str2)) if char1 != char2), None)
        return index               
    
    def bfs_toposort(self, start, graph) -> List[str]:
        q = []
        q.append(start)
        topo_sort = []
        visited = set()
        parent = {}
        while len(q) > 0:
            cur = q.pop(0)
            topo_sort.append(cur)
            for c in graph[cur]:
                if c not in visited:
                    visited.add(c)
                    q.append(c)
        return topo_sort
    
    def alienOrder(self, words: List[str]) -> str:
        alphabet = set(''.join(words)) # all unique characters
        print("alphabet: ", alphabet)
        alphabet = sorted(list(alphabet))
        print("alphabet: ", alphabet)
        alphabet_map = {a: i for i, a in enumerate(alphabet)}
        
        # create an adjacency matrix
        adj = [[0]*len(alphabet) for _ in range(len(alphabet))]
        
        # iterate through the list once for first letters
        cur_char = words[0][0]
        for word in words:
            if word[0] != cur_char:
                adj[alphabet_map[cur_char]][alphabet_map[word[0]]] = 1
                cur_char = word[0]
        
        # now compare adjacent items
        for i in range(1,len(words)):
            # compare words[i] and words[i-1]
            index = self.index_diff(words[i], words[i-1])
            if index is not None:
                adj[alphabet_map[words[i-1][index]]][alphabet_map[words[i][index]]] = 1
        
        g_edges = {a: [] for a in alphabet}
        for i in range(len(alphabet)):
            for j in range(len(alphabet)):
                if adj[i][j] == 1:
                    g_edges[alphabet[i]].append(alphabet[j])
        
        # now create an ordering
        topo_sort = self.bfs_toposort(words[0][0], g_edges)
        diff = set(alphabet) - set(topo_sort)
        topo_sort.extend(list(diff))
        
        return ''.join(topo_sort)
