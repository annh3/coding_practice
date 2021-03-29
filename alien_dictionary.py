class Solution:
    def index_diff(self, str1, str2):
        index = next((i for i, (char1, char2) in enumerate(zip(str1, str2)) if char1 != char2), None)
        return index  
    
    def DFS(self, cur, g, visited, in_process):
        if cur == None or cur in visited:
            return False

        in_process.add(cur)

        flag = False
        for child in g[cur]:
            if child in in_process:
                return True
            if child not in visited:
                flag = flag or self.DFS(child, g, visited, in_process)
        in_process.remove(cur)
        visited.add(cur)
        return flag

    def DFS_wrapper(self, cur, g):
        visited = set()
        in_process = set()
        res = False
        for node in g.keys():
            res = res or self.DFS(node, g, visited, in_process)
        return res
    
    def topo_sort(self,g): # a dictionary adjacency list

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
            if index is None and len(words[i-1]) > len(words[i]):
                return ""
        
        g_edges = {a: [] for a in alphabet}
        for i in range(len(alphabet)):
            for j in range(len(alphabet)):
                if adj[i][j] == 1:
                    g_edges[alphabet[i]].append(alphabet[j])
        print("g_edges: ", g_edges)
        
        # cycle detection
        res = self.DFS_wrapper(words[0][0], g_edges)
        if res == True:
            return ""
        
        # now create an ordering
        topo_sort = self.topo_sort(g_edges)    
        diff = set(alphabet) - set(topo_sort)
        topo_sort.extend(list(diff))
        
        return ''.join(topo_sort)
