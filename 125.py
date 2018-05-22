class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new = ''
        for i in range(len(s)):
            if s[i].isalnum():
                new += s[i]
                
        return new == new[::-1]
