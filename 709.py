class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for x in str:
            if 'A' <= x <= 'Z':
                res += chr(ord(x) + 32)
            else:
                res += x
        return res
