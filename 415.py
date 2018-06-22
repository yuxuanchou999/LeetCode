class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        res, i, j, carry = [], len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1
            res.append(str(carry % 10))
            carry //= 10
            
        return ''.join(res[::-1])
