class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans, idx = len(s) - 1, 1
        for i in range(len(s)):
            if s[:i + 1] == s[:i + 1][::-1]:
                if ans > len(s) - i - 1:
                    ans = len(s) - i - 1
                    idx = i + 1
        return s[idx:][::-1] + s
            
