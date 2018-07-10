class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(new, i, j, ans):
            if j == k and ans == n: 
                res.append(new)
                return
            if j >= k: return
            for x in range(i, 10):
                if x + ans  <= n:
                    helper(new + [x], x + 1, j + 1, ans + x)
                    
        
        res = []
        for i in range(1, 10):
            helper([i], i + 1, 1, i)
            
        return res
