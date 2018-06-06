class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        res = [sign + str(n), '.']
        stack = []
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(10 * remainder, abs(denominator))
            res.append(str(n))
        
        res.insert(stack.index(remainder) + 2, '(')
        res.append(')')
        return ''.join(res).replace('(0)', '').rstrip('.')
