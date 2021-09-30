
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0

        def dfs(root):
            nonlocal sum

            if root is None:
                return

            elif root.val == low:
                sum += root.val
                dfs(root.right)

            elif root.val == high:
                sum += root.val
                dfs(root.left)

            elif root.val > low and root.val < high:  # 사이일 때
                sum += root.val
                dfs(root.left)
                dfs(root.right)

            elif root.val < low:  # low 보다 작을 때
                dfs(root.right)

            else:  # height 보다 클 때
                dfs(root.left)

        dfs(root)

        return sum


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(root):

            if root is None:
                return 0

            elif root.val == low:
                return root.val + dfs(root.right)

            elif root.val == high:
                return root.val + dfs(root.left)

            elif root.val > low and root.val < high:  # 사이일 때
                return root.val + dfs(root.left) + dfs(root.right)

            elif root.val < low:  # low 보다 작을 때
                return dfs(root.right)

            else:  # height 보다 클 때
                return dfs(root.left)


        return dfs(root)


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], L: int, R: int) -> int:
        stack, sum = [root], 0

        while stack:
            node = stack.pop()
            if node:
                if node.val < L:
                    stack.append(node.right)
                elif node.val > R:
                    stack.append(node.left)
                else:
                    sum += node.val
                    stack.append(node.left)
                    stack.append(node.right)

        return sum