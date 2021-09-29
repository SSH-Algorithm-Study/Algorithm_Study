class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    sum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def inorder_traversal(root):
            if root is None:
                return

            inorder_traversal(root.right)
            self.sum += root.val
            root.val = self.sum
            inorder_traversal(root.left)

        inorder_traversal(root)

        return root
