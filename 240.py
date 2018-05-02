class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nr = len(matrix)
        for i in range(nr):
            if not matrix[i]: return False
            if matrix[i][0] <= target <= matrix[i][-1]:
                if target in matrix[i]: 
                    return True
            continue
                
        return False
