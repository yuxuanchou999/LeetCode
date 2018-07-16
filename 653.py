class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        stk, res = [root], []
        while stk:
            x = stk.pop(0)
            if k - x.val in res: return True
            res.append(x.val)
            if x.left: stk.append(x.left)
            if x.right: stk.append(x.right)
        return False
