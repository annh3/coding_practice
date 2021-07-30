import collections
Tree = lambda: collections.defaultdict(Tree) # oh wow you can literally name this anything
WEIGHT = False
import pdb
"""

"""

class WordFilter(object):
    def __init__(self, words):
        self.trie1 = Tree() #prefix
        self.trie2 = Tree() #suffix
        for weight, word in enumerate(words):
            cur = self.trie1

            # First, add the current word to the top of the prefix tree, cur
            # [FALSE] -> {idx1, idx2,...}
            self.addw(cur, weight)
            # Then, 
            for letter in word:
                # change cur to be the Tree stored at cur[letter]
                # how is this ok?
                # defaultdict thing... try more implementations
                cur = cur[letter]
                self.addw(cur, weight)

            cur = self.trie2
            self.addw(cur, weight)
            for letter in word[::-1]:
                cur = cur[letter]
                self.addw(cur, weight)

    """
    We never change the global value of WEIGHT, set to False

    [FALSE] -> {index}

    Otherwise, we've stepped into the key 'letter', and create a new
    Default dict there 

    We can step into this later
    """
    def addw(self, node, w):
        if WEIGHT not in node:
            # we've traversed to the end of this path
            node[WEIGHT] = {w}
        else:
            # add to list of words that share this prefix
            node[WEIGHT].add(w)
            #pdb.set_trace()

    def f(self, prefix, suffix):
        cur1 = self.trie1
        for letter in prefix:
            if letter not in cur1: return -1
            cur1 = cur1[letter]

        cur2 = self.trie2
        for letter in suffix[::-1]:
            if letter not in cur2: return -1
            cur2 = cur2[letter]

        pdb.set_trace()
        return max(cur1[WEIGHT] & cur2[WEIGHT])
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

def test1():
    list_of_strings = ['apple', 'candle', 'listserve', 'grace', 'icecream', 'luxury', 'travel']
    word_filter = WordFilter(list_of_strings)
    res = word_filter.f('tr','el') # should return 6
    print("result of search: ", res)


if __name__ == "__main__":
    test1()

