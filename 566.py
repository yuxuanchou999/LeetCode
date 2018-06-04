class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c > len(nums) * len(nums[0]): return nums
        a = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        k, res = 0, []
        for i in range(r):
            new = []
            for j in range(c):
                new.append(a[k])
                k += 1
            res.append(new)
            
        return res
