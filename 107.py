# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        stk, new, res = [root], [], [[root.val]]
        while stk:
            x = stk.pop(0)
            if x.left: new.append(x.left)
            if x.right: new.append(x.right)
            if not stk:
                if new:
                    res.append([node.val for node in new])
                stk = new
                new = []
        return res[::-1]

                
            
        
