class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) < len(p) - p.count('*'): return False
        dp = [True] + [False] * len(s)
        for i in p:
            if i != '*':
                for j in reversed(range(len(s))):
                    dp[j + 1] = dp[j] and (s[j] == i or i == '?')
            else:
                for j in range(1, len(s) + 1):
                    dp[j] = dp[j] or dp[j - 1]
            dp[0] = dp[0] and i == '*'
            
        return dp[-1]
                    
