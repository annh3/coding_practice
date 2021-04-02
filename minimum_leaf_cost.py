class Solution:
    def dp(self, i, j, arr: List[int], cache):
        if (i,j) in cache:
            return cache[(i,j)]
        if i >= j:
            return 0
        
        res = float('inf')
        for k in range(i+1,j+1):
            # print("i: ", i)
            # print("k: ", k)
            # print("j: ", j)
            # print("\n")
            res = min(res, self.dp(i,k-1, arr, cache) + self.dp(k,j, arr, cache) + max(arr[i:k])*max(arr[k:j+1]))
        cache[(i,j)] = res
        return res
        
        
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cache = {}
        res = self.dp(0, len(arr)-1, arr, cache)
        return res
