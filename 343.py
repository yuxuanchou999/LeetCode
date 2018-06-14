class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1

        # integerBreak(n) = max(integerBreak(n - 2) * 2, integerBreak(n - 3) * 3)
        res = [0, 1, 2, 3]
        for i in range(4, n + 1):
            res[i % 4] = max(res[(i - 2) % 4] * 2, res[(i - 3) % 4] * 3)
        return res[n % 4]
