# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return None
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        vals = []
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split()
        root = TreeNode(int(data.pop(0)))
        head = root
        while data:
            root = head
            v = int(data.pop(0))
            while root:
                if root.val > v:
                    if root.left:
                        root = root.left
                    else:
                        root.left = TreeNode(v)
                        break
                else:
                    if root.right:
                        root = root.right
                    else:
                        root.right = TreeNode(v)
                        break
            
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
