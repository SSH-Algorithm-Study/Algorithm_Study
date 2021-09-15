class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        state = 0
        def dfs(root1, root2):
            nonlocal state
            if root1 is None and root2 is None: # 둘다 null일경우
                return
            if root1 is None: # root1만 null일 경우
                state = 1
                return
            if root2 is None: # root2만 null일 경우
                return
            root1.val = root2.val + root1.val # root1, root2 둘다 null이 아닐경우

            dfs(root1.left, root2.left)
            if state == 1:
                root1.left = root2.left
                state = 0
            dfs(root1.right, root2.right)
            if state == 1:
                root1.right = root2.right
                state = 0


        dfs(root1, root2)
        if state == 1:  # root1이 빈값으로 들어가면
            return root2
        else:
            return root1


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2 # 둘중하나가 null일때 null아닌값 넘겨주기