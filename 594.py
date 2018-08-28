class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        ans = 0
        for x in sorted(set(nums)):
            ans = max(c[x] + c[x + 1], ans) if x + 1 in c else ans
        return ans
