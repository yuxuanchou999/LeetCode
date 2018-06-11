class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def helper(a, b):
            if len(b) + len(a) < k:return
            if len(a) == k:
                res.append(a)
                return
            for x in b:
                helper(a + [x], range(x + 1, n + 1))
            
            
        res = []
        for x in range(1, n + 2 - k):
            helper([x], range(x + 1, n + 1))
        return res
