class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt, element = 0, set(nums)
        for x in element:
            if k == 0  and nums.count(x) > 1: cnt += 1
            if k > 0 and x + k in element:
                cnt += 1
                
        return cnt
        
