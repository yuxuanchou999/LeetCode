class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        res = [[False] * n for _ in range(n)]
        r = c = di = 0
        for i in range(1, n * n + 1):
            res[r][c] = i
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and res[cr][cc] == False:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
        return res
