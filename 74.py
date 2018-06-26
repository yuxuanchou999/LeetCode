class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(len(matrix)):
            if i == len(matrix) - 1:
                if target in matrix[i]:
                    return True
                return False
            else:
                if matrix[i][0] <= target < matrix[i + 1][0]:
                    if target in matrix[i]:
                            return True
                        
        return False
                    
