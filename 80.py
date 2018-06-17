class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, j, pre = 0, 0, None
        for i in range(len(nums)):
            if pre is None or nums[i] != pre:
                pre = nums[i]
                cnt = 1
                nums[j] = nums[i]
                j += 1
            else:
                if cnt < 2:
                    cnt += 1
                    nums[j] = nums[i]
                    j += 1
        return j
                    
            
