# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 빈 연결리스트 예외처리
        if head is None :
            return head

        list = []

        while head != None :
            list.append(head.val)
            head = head.next

        result = ListNode()
        p1 = result
        p1.val = list.pop()

        while list:
            p1.next = ListNode(list.pop())
            p1 = p1.next


        return result


# is -> 같은 객체일때
# bool()연산으로 참거짓 알수있음
# 빈 리스트 if not list /  if list
# [] is True x
