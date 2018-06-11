class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(queens, xy_sum, xy_dif):
            p = len(queens)
            if p == n:
                res.append(queens)
                return None
            for q in range(n):
                if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queens + [q], xy_sum + [p + q], xy_dif + [p - q])
                    
        res = []
        DFS([], [], [])
        return len(res)
            
