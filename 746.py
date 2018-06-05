class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * 3
        for i in reversed(range(len(cost))):
            dp[i % 3] = cost[i] + min(dp[(i + 1) % 3], dp[(i + 2) % 3])
        return min(dp[0], dp[1])
