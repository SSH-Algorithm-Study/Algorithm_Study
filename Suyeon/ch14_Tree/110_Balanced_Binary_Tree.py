# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        state = 0

        def dfs(root):
            nonlocal state
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                state = 1

            return max(left, right) + 1

        dfs(root)

        return state == 0


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1
