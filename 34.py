class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.BS(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, self.BS(nums, target, False) - 1]
    
    def BS(self, nums, target, left):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target or (left and nums[mid] == target):
                r = mid
            else:
                l = mid + 1
        return l
                
