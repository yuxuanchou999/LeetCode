class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i
            else:
                dic[nums[i]] = [1, i, i]
        maxl = collections.Counter(nums).most_common()[0][1]
        # maxl = 0
        # for key in dic:
        #     maxl = max(maxl, dic[key][0])
        
        degree = 2 ** 31 - 1
        for key in dic:
            if dic[key][0] == maxl:
                degree = min(degree, dic[key][2] - dic[key][1] + 1)
                
        return degree
