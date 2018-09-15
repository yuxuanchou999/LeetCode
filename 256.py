class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(costs)):
            for j in range(3):
                costs[i][j] += min(costs[i - 1][k] for k in range(3) if k != j)
        return min(costs[-1][j] for j in range(3)) if costs else 0
