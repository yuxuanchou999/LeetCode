class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        i = nums.index(max(nums))
        root = TreeNode(nums[i])
        root.left = self.constructMaximumBinaryTree(nums[:i]) if i > 0 else None
        root.right = self.constructMaximumBinaryTree(nums[i + 1:]) if i < len(nums) else None
        return root
