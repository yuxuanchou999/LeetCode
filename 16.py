class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res, tot = 2 ** 31 - 1, 0
        nums.sort()
        for i in range(len(nums)):
            ans = nums[i]
            l, r = i + 1, len(nums) -1
            while l < len(nums) and l < r:
                curr = ans + nums[l] + nums[r]
                if curr == target: return target
                elif curr > target: r -= 1
                else: l += 1
                if abs(curr - target) < res:
                    res = abs(curr - target)
                    tot = curr
                     
        return tot
            
                    
                    
                    
