class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n:
            s += chr((n - 1) % 26 + ord('A'))
            n = (n - 1) // 26
            
        return s[::-1]
            
