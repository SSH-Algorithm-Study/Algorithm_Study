class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right, root.left

        dfs(root)

        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left , root.right = self.invertTree(root.right), self.invertTree(root.left)

            return root

