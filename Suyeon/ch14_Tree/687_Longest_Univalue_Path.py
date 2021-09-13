class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root):
            nonlocal result
            c = 0  # 루르토드에서 까지의 최대 count수
            next_c = 0 # 넘겨줄 count
            if root is None:
                return (1001, 0)

            node, count = dfs(root.left)
            if root.val == node: # 왼쪽자식이 루트값과 같을때
                c += count + 1
                next_c = count + 1
            node, count = dfs(root.right)
            if root.val == node:  # 오른쪽자식이 루트값과 같을때
                c += count + 1
                next_c = max(next_c, count + 1) # 둘다 같으면 더 큰쪽
            result = max(result, c)

            return (root.val, next_c )



        node, count = dfs(root)
        return max(result, count) #마지막 루트값까지 max따져주기


