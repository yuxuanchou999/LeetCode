class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(n):
            ans = 1
            for i in range(1, n):
                ans *= i
            return ans
        
        res, nums = '', [str(i) for i in range(1, n + 1)]
        while n:
            res += nums[k // (helper(n))] if k % helper(n) else nums[k // (helper(n)) - 1]
            k %= helper(n)
            n -= 1
            nums.remove(res[-1])
        return res
