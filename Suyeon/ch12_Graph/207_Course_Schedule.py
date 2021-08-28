class ListNode:
    def __init__(self, val=None, state = 0, pre=None ):
        self.state = state
        self.pre = pre
        self.val = val

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        root = ListNode()
        p = root

        for prerequisite in prerequisites:
            p.pre = ListNode(val = prerequisite[0], pre = prerequisite[1])
            p = p.pre


