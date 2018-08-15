class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        pre, avoid, using = None, 0, 0
        for k in sorted(count):
            if k - 1 != pre:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            pre = k
        return max(avoid, using)
