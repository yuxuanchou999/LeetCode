class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.floor((math.sqrt(1 + 8 * n) - 1) // 2)
