class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, b = float('inf'), float('inf')
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                b = c
            else:
                return True
        return False
