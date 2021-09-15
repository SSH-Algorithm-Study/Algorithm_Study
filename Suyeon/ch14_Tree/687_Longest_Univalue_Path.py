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
                return 0

            count = dfs(root.left)
            if root.left and root.val == root.left.val: # 왼쪽자식이 루트값과 같을때
                c += count + 1
                next_c = count + 1
            count = dfs(root.right)
            if root.right and root.val == root.right.val:  # 오른쪽자식이 루트값과 같을때
                c += count + 1
                next_c = max(next_c, count + 1) # 둘다 같으면 더 큰쪽
            result = max(result, c)

            return next_c



        dfs(root)
        return result



class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root):
            nonlocal result
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            if root.left and root.val == root.left.val: # 왼쪽자식이 루트값과 같을때
                left += 1
            else:  # 값이 다르다면 0으로 초기화
                left = 0
            if root.right and root.val == root.right.val:  # 오른쪽자식이 루트값과 같을때
                right += 1
            else:  # 값이 다르다면 0으로 초기화
                right = 0


            result = max(result, left+right)

            return max(right, left)



        dfs(root)
        return result


