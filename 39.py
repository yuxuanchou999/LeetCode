class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.findnext(sorted(candidates), target, [], res)
        return res
    
    def findnext(self, nums, target, path, res):
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < target:
                self.findnext(nums[:i + 1], target - nums[i], path + [nums[i]], res)
            if nums[i] == target:
                res.append(path + [nums[i]])


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, path, index):
            if remain == 0:
                res.append(path)
            for i in range(index, len(cand)):
                if cand[i] > remain:
                    break
                dfs(remain - cand[i], [cand[i]] + path, i)

        res = []
        cand = sorted(candidates)
        dfs(target, [], 0)
        return res
        
