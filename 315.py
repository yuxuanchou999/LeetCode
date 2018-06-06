class BIT(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)
        
    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & (-i)
            
    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i &(-i)
        return r
        
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashTable = {v:i for i, v in enumerate(sorted(set(nums)))}
        tree, r = BIT(len(hashTable)), []
        for i in reversed(range(len(nums))):
            r.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1, 1)
        return r[::-1]
