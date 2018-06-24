class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[left] and nums[left] <= target < nums[mid] or\
            (nums[left] > nums[mid] and not nums[mid] < target <= nums[right]):
                right = mid -1
            else:
                left += 1
                
        return False
