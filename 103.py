# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        i, new, cur, res = 0, [], [root], [[root.val]]
        while cur:
            x = cur.pop()
            if not i % 2:
                if x.right: new.append(x.right)
                if x.left: new.append(x.left)
            else:
                if x.left: new.append(x.left)
                if x.right: new.append(x.right)
            if not cur and new:
                res.append([node.val for node in new])
                cur = new
                new = []
                i += 1
                
        return res
                
