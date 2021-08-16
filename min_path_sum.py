class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cache = {}
        m = len(grid)
        n = len(grid[0])
        
        def dp_solution(cur):
            # if cur[0] >= m or cur[1] >= n:
            #     return 10000
            
            if cur == (m-1,n-1):
                return grid[m-1][n-1]
            
            if cur in cache:
                return cache[cur]
            
            print("exploring: ", cur)
            
            cost = m*n
            type1 = m*n
            type2 = m*n
            
            if cur[0] < m and cur[1] < n: # move right
                if cur[1] < n:
                    type1 = grid[cur[0]][cur[1]] + dp_solution((cur[0], cur[1]+1))
                if cur[0] < m:
                    type2 = grid[cur[0]][cur[1]] + dp_solution((cur[0]+1, cur[1]))
            
            print("for ", cur, "  min is ", min(type1, type2))
            cache[cur] = min(type1, type2)
            
            return min(type1, type2)
        
        return dp_solution((0,0))
