class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2: return 0
        if k >= n / 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        globalmax = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            localmax = [0] * n
            for j in range(1, n):
                pro = prices[j] - prices[j - 1]
                localmax[j] = max(pro + globalmax[i - 1][j - 1], globalmax[i - 1][j - 1], pro + localmax[j - 1])
                globalmax[i][j] = max(globalmax[i][j - 1], localmax[j])
        return globalmax[-1][-1]
