class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans, col = 0, []
        for j in range(len(grid[0])):
            col.append(max([grid[k][j] for k in range(len(grid))]))
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans += min(col[j], max(grid[i])) - grid[i][j]
                
        return ans
