# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def helper(low, high):
            res = []
            if low > high: 
                res.append(None)
            for i in range(low, high + 1):
                left = helper(low, i - 1)
                right = helper(i + 1, high)
                for j in left:
                    for k in right:
                        cur = TreeNode(i)
                        cur.left = j
                        cur.right = k
                        res.append(cur)
                        
            return res
                
        return helper(1, n) if n else []
            
        
            
