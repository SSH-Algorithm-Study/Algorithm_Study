# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxheight(root):
            if root is None:
                return 0
            left = maxheight(root.left)
            right = maxheight(root.right)
            self.result = max(Solution.result, left + right)
            return max(left, right) + 1

        maxheight(root)

        return self.result # 중첩함수에서 자식함수가 부모함수의 값을 재할할 수 없기 때문에 클래스변수로 선언