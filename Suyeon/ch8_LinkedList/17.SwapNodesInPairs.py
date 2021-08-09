# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         p = head
#         if p is not None and p.next is not None:
#             # 처음일경우 (head == p)
#             q = p.next
#             head = q  # head값 바꿔줌
#             p.next = q.next
#             q.next = p
#             r = p  # 앞으로 가기전 p값 저장
#             p = p.next  # p이동
#
#             # 처음 아닐경우
#             while p is not None and p.next is not None:
#                 q = p.next
#                 p.next = q.next
#                 q.next = p
#                 r.next = q
#                 r = p  # 앞으로 가기전 p값 저장
#                 p = p.next  # p이동
#
#         return head


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # swap
            b = head.next
            head.next = b.next
            b.next = head

            # 이전 prev가 b가리키기
            prev.next = b

            # 이동
            head = head.next
            prev = prev.next.next

        return root.next