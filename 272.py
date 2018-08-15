# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        inorder = []
        inorder(root)
        result = inorder[:k]
        for i in range(k,len(inorder)):
            if abs(result[0] - target) > abs(inorder[i] - target):
                result.append(inorder[i])
                result=result[1:]
            else:
                return result
        return result

        
