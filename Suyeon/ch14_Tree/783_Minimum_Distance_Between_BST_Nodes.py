# Definition for a binary tree node.
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_value = sys.maxsize
        before = sys.maxsize  # 이전값 저장

        def travel(root):
            nonlocal min_value
            nonlocal before
            if root is None:
                return

            travel(root.left)
            min_value = min(abs(before-root.val) , min_value)  # 현재 값과 이전값의 차로 최소값 갱신 
            before = root.val  # 이전값으로 갱신
            travel(root.right)

        travel(root)

        return min_value