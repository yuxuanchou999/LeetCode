class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        n = [1, 1]
        for i in range(2, rowIndex + 1):
            for j in range(len(n) - 1):
                n[j] = n[j] + n[j + 1]
            n = [1] + n
        return n
                
