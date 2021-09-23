class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(head, tail):
            if head > tail :
                return
            root = TreeNode()
            mid = (head+tail) // 2
            root.val = nums[mid]  # 중간값을 기준으로 루트노드를 잡는다

            root.left = dfs( head, mid-1)
            root.right = dfs( mid+1, tail)

            return root

        result = dfs(0, len(nums)-1)

        return result



