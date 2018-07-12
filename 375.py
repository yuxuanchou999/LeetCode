class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(n + 1)]
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                dp[i][j] = min(k + 1 + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i, j + 1))
                
        return dp[0][n - 1]
        
