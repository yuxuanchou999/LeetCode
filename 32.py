class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')':
                if stack:
                    dp[i], dp[stack.pop(-1)] = 1, 1
            else:
                stack.append(i)
            
        for i in range(1, len(dp)):
            if dp[i] > 0:
                dp[i] += dp[i - 1]
                
        
        return max(dp) if dp else 0
