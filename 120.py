class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        Bottom-up:
        minpath = list(triangle[-1])
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                minpath[j] = min(minpath[j], minpath[j + 1]) + triangle[i][j]
                
        return minpath[0



        Top-down:
	res = [[0 for _ in row] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j ==  len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j], res[i - 1][j - 1]) + triangle[i][j]
                    
        return min(res[-1])
