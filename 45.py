class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) == 1: return len(nums) - 1
        cnt, end = 0, len(nums) - 1
        while end != 0:
            for i in range(end):
                if i + nums[i] >= end:
                    cnt += 1
                    end = i
                    break
                    
        return cnt
                    
                    
                
