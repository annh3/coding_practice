class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes_tree = {c: {} for c in string.ascii_lowercase}
        
        for i,word in enumerate(words):
            word = word.lower()
            cur = self.prefixes_tree
            for l in word:
                if l in cur:
                    cur = cur[l]
                else:
                    cur[l] = {}
                    cur = cur[l]
            cur['*'] = {i}
        
        self.suffixes_tree = {c: {} for c in string.ascii_lowercase}
        
        for i,word in words:
            word = reversed(word).lower()
            cur = self.suffixes_tree
            for l in word:
                if l in cur:
                    cur = cur[l]
                else:
                    cur[l] = {}
                    cur = cur[l]
            cur['*'] = {i}
        

    def f(self, prefix: str, suffix: str) -> int:
        suffix_idx = -1
        prefix_idx = -1
        
        # search prefix tree
        cur = self.prefixes_tree
        broke_out = False
        
        for l in prefix:
            cur = cur[l]
        else:
            broke_out = True
            
        if not broke_out and '*' in cur:
            prefix_idx = cur['*']
            
            
        # search suffix tree
        cur = self.suffixes_tree
        broke_out = False
        
        for l in suffix:
            cur = cur[l]
        else:
            broke_out = True
            
        if not broke_out and '*' in cur:
            suffix_idx = cur['*']
            
        return max(prefix_idx, suffix_idx)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
