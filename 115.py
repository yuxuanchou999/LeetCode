class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        l1, l2 = len(s), len(t)
        dp = [0 for _ in range(l2 + 1)]
        dp[0] = 1
        for i in range(1, l1 + 1):
            diag = 1
            for j in range(1, l2 + 1):
                dp[j], diag = dp[j] + diag * (t[j - 1] == s[i - 1]), dp[j]

        return dp[-1]
