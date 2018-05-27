class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        dp = [1] + [0] * (len(nums) - 1)
        if max([nums[i] + i for i in range(len(nums) - 1)]) < len(nums) - 1: return False
        for i in range(len(nums)):
            if dp[i]:
                if nums[i] + i >= len(nums) - 1: return True
                for j in range(i + 1, i + nums[i] + 1):
                    dp[j] = 1
            
        return False
            
                
            
                
