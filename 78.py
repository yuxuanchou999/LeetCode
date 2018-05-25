class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper([], sorted(nums))
        
    def helper(self, cur, nums):
        if not nums:
            return [cur]
        return self.helper(cur, nums[1:]) + self.helper(cur + [nums[0]], nums[1:])
    
        
        
