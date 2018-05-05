class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coins = [1] + [i for i in nums if i > 0] + [1]
        n = len(coins)
        max_coin = [[0 for _ in range(n)] for _ in range(n)]
        for k in range(2, n):
            for left in range(n - k):
                right = left + k
                for i in range(left + 1, right):
                    max_coin[left][right] = max(max_coin[left][right], coins[left] * coins[i] * coins[right] + \
                                             max_coin[left][i] + max_coin[i][right])
                
        return max_coin[0][-1]
