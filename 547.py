class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(j)
                    
        cnt, visited = 0, [0] * len(M)
        for i in range(len(M)):
            if not visited[i]:
                dfs(i)
                cnt += 1
            
        return cnt
