class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes_tree = {c: {'idxs': [], 'tree':{}} for c in string.ascii_lowercase}
        for i,word in enumerate(words):
            word = word.lower()
            cur = self.prefixes_tree[word[0]]
            for l in word[1:]:
                if l in cur:
                    cur['idxs'].append(i)
                    cur = cur['tree'][l]
                    
                else:
                    cur[l] = {'idxs': [], 'tree':{}}
                    cur[l]['idxs'].append(i)
                    cur = cur[l]['tree']
            #cur['*'] = {i}
        
        self.suffixes_tree = {c: {} for c in string.ascii_lowercase}
        
        for i,word in enumerate(words):
            word = word[::-1]
            word = word.lower()
            cur = self.suffixes_tree[word[0]]
            for l in word[1:]:
                if l in cur:
                    cur['idxs'].append(i)
                    cur = cur['tree'][l]
                    
                else:
                    cur[l] = {'idxs': [], 'tree':{}}
                    cur[l]['idxs'].append(i)
                    cur = cur[l]['tree']
        

    def f(self, prefix: str, suffix: str) -> int:
        suffix_idx = -1
        prefix_idx = -1
        print("exists: ", len(self.prefixes_tree))
        # search prefix tree
        cur = self.prefixes_tree
        broke_out = False
        print("prefix: ", prefix)
        for l in prefix:
            print("l: ", l)
            if l in cur:
                cur = cur[l]['tree']
                #print("cur length: ", len(cur))
            else:
                print("breaking out")
                broke_out = True
        
        print("cur at bottom: ", cur)
        if not broke_out:
            # traverse the tree
            prefix_idx = max(cur['idxs'])
            
            
        # search suffix tree
        cur = self.suffixes_tree
        broke_out = False
        
        for l in suffix:
            if l in cur:
                cur = cur['tree'][l]
            else:
                broke_out = True
            
        if not broke_out:
            suffix_idx = max(cur['idxs'])
            
        return max(prefix_idx, suffix_idx)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
