class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, acc = 0, 0
        lookup = collections.defaultdict(int)
        lookup[0] += 1
        for n in nums:
            acc += n
            res += lookup[acc - k]
            lookup[acc] += 1
        return res
