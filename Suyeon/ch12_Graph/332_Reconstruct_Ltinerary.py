class ListNode:

    def __init__(self,val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        num = len(tickets)

        for ticket in tickets:
            head = ListNode