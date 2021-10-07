# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        root = TreeNode(root_val)
        if root_idx != 0: # 왼쪽자식이 있을 때
            root.left = self.buildTree(preorder=preorder[1:1 + root_idx], inorder=inorder[:root_idx]) 
        if root_idx != len(inorder) - 1:  # 오른쪽 자식이 있을 때
            root.right = self.buildTree(preorder=preorder[1 + root_idx:], inorder=inorder[root_idx + 1:])

        return root

