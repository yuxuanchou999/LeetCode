class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return n
        cnt = 0
        while n > 0:
            n -= 9 * (10**cnt) * (cnt + 1)
            cnt += 1
        n += 9 * (10**(cnt - 1)) * cnt
        return int(str(10 ** (cnt - 1) + n // cnt - 1)[-1]) if n % cnt == 0 \
            else int(str(10 ** (cnt - 1) + n // cnt)[n % cnt - 1])
        
