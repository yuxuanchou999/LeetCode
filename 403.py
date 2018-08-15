class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        if stones[1] != 1: return False
        units = {s: set() for s in stones}
        units[1].add(1)
        for i in stones[:-1]:
            for k in units[i]:
                for j in (k, k - 1, k + 1):
                    if j > 0 and j + i in units:
                        units[j + i].add(j)
                        
        return bool(units[stones[-1]])
