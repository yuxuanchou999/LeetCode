class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        num = [x for y in matrix for x in y]
        return sorted(num)[k - 1]
