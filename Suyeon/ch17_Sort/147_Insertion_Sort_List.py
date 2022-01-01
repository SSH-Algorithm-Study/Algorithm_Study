# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slist = ListNode()  # 더미
        slist.next = ListNode(head.val)
        head = head.next

        while head: # head가 끝나기 전까지
            p = slist
            new_node = ListNode(head.val) # 초기 세팅
            head = head.next
            while p.next: # p가 안끝난경우
                if p.next.val < new_node.val:
                    p = p.next
                else:
                    new_node.next = p.next
                    p.next = new_node
                    break
            if not p.next: # p가 끝난경우
                p.next = new_node

        return slist.next

