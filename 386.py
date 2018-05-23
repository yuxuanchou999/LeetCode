class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a = sorted([str(i) for i in range(1, n + 1)])
        return [int(i) for i in a]
