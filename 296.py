class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        total = 0
        for grid in grid, zip(*grid):
            X = []
            for x, row in enumerate(grid):
                X += [x] * sum(row)
            total += sum(abs(x - X[len(X) // 2])
                         for x in X)
        return total
