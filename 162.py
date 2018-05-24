class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [-2 ** 31] + nums + [-2 ** 31]
        for i in range(1, len(nums) - 1):
            if max(nums[i - 1:i + 2]) == nums[i]:
                return i - 1
