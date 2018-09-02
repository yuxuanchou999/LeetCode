class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        return min(x[0] for x in ops) * min(x[1] for x in ops) if ops else m * n
