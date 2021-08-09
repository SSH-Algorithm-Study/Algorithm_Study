# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:  # 빈 연결리스트 거르기
            p = head
            even = head.next    # 첫 짝수번째 head 저장
            q = head.next

            while q is not None:  # 짝수 끝검사
                p.next = q.next
                if p.next is not None:    # 마지막 홀수 아닐때만
                    p = p.next
                else:  # 마지막 홀수번재면 루프탈출
                    break
                q.next = p.next
                q = q.next

            p.next = even   # 홀수 끝 짝수 첫으로 이어주기 

        return head


