class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(i, j):
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == ans:
                image[i][j] = newColor
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i - 1, j)
        
        ans = image[sr][sc]
        if ans == newColor: return image
        dfs(sr, sc)
        return image
