class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s[0] == '0': return 0
        dp = [1] + [0] * (len(s) - 1)
        if len(s) > 1:
            if s[:2] > '26': 
                dp[1] = 1 if s[1] != '0' else 0
            else:
                dp[1] = 2 if s[1] != '0' else 1
            for i in range(2, len(s)):
                if s[i - 1:i + 1] > '26':
                    if s[i] == '0':
                        return 0
                    dp[i] = dp[i - 1]
                else:
                    if s[i] == '0':
                        if s[i - 1] == '0':
                            return 0
                        dp[i] = dp[i - 2]
                    else:
                        if s[i - 1] != '0':
                            dp[i] = dp[i - 1] + dp[i - 2]
                        else:
                            dp[i] = dp[i - 1]
                
        return dp[-1]
