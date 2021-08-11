class Solution:
    def validEdge(self,i,j,i_new, j_new, m,n, matrix):
        if not( 0 <= i_new < m and 0 <= j_new < n):
            return False
        # check value
        if matrix[i][j] > matrix[i_new][j_new]:
            return False
        
        return True
        
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        m = len(matrix)
        # m by n
    
        overall_maxval = 0
        
        def DFS(i,j, visited):
            # (i,j) represents a cell
            maxval = 1
            print("DFS called on: ", i, j)
            
            for di, dj in [(-1,0), (0,-1), (1,0), (0,1)]:
                if self.validEdge(i,j, i+di, j+dj, m, n, matrix) and (i+di,j+dj) not in visited:
                    print("traversing")
                    visited.add((i+di, j+dj))
                    val = 1 + DFS(i+di, j+dj, visited)
                    if val > maxval:
                        maxval = val
            print("returning maxval: ", maxval)
            return maxval
        
        for i in range(m):
            for j in range(n):
                visited = set()
                curval = DFS(i,j,visited)
                if curval > overall_maxval:
                    overall_maxval = curval
                    
        return overall_maxval
