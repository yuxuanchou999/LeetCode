class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = [0]
        for num in nums:
            self.n.append(self.n[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.n[j + 1] - self.n[i]
