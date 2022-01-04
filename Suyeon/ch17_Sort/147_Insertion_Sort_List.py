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

# 한줄로 쓰기
# p.next가 끝나던 p.next.val >= head.val이여서 자리를 찾던 넣어줘야한다 -> 합치기
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = slist = ListNode()

        while head:
            while p.next and p.next.val < head.val: # p값이 head값보다 작으면
                p = p.next

            p.next, head.next, head = head, p.next, head.next   # 중간에 삽입

            p = slist

        return slist.next

#비교개선
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = slist = ListNode()

        while head:
            while p.next and p.next.val < head.val:  # p값이 head값보다 작으면
                p = p.next

            p.next, head.next, head = head, p.next, head.next

            if head and p.next.val > head.val: # 정렬한것중 최대값보다 작다면
                p = slist # 처음부터 비교

        return slist.next


