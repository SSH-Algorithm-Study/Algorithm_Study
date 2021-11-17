# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, h1, h2):
        new = ListNode()
        p = new

        while h1 and h2 :
            if h1.val > h2.val:
                p.next = h2
                h2 = h2.next
            else:
                p.next = h1
                h1 = h1.next
            p = p.next

        if h1:
            p.next = h1
        if h2:
            p.next = h2

        return new.next


    def mergeSort(self, first):

        if first is None or first.next is None:
            return first

        slow = fast = bef = first

        while fast and fast.next:
            bef = slow
            slow = slow.next
            fast = fast.next.next

        bef.next = None # 분리

        h1 = self.mergeSort(first)
        h2 = self.mergeSort(slow)
        return self.merge(h1, h2)



    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)




class Solution:
    def merge(self, h1, h2):
        if h1 and h2:
            if h1.val > h2.val:
                h1, h2 = h2, h1
            h1.next = self.merge(h1.next, h2)

        return h1 or h2

    def mergeSort(self, first):

        if first is None or first.next is None:
            return first

        slow = fast = bef = first

        while fast and fast.next:
            bef = slow
            slow = slow.next
            fast = fast.next.next

        bef.next = None  # 분리

        h1 = self.mergeSort(first)
        h2 = self.mergeSort(slow)
        return self.merge(h1, h2)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)