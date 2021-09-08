import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxheight(root):
            if root is None:
                return 0
            return max(maxheight(root.left), maxheight(root.right)) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()

        if root is None: #루트예외처리
            return 0
        queue.append(root)
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)): # 부모노드만큼만 돌기위해 처음엔 queue엔 항상 부모만 들어있다 이후에 섞인다
                p = queue.popleft() # p가 none인것이 애초에 들어올수없게
                if p.left is not None: # none이 아닌 자식들만 추가
                    queue.append(p.left)
                if p.right is not None:
                    queue.append(p.right)

        return depth
