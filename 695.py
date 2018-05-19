class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area, nr, nc = 0, len(grid), len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < nr and 0 <= j < nc and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i - 1, j)
            return 0
            
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
                    
        return area
