import functools
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(n1, n2, carry):
            sum = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            return (sum, carry)

        p1 = l1
        p2 = l2
        result = ListNode()
        p3 = result
        carry = 0 # 올림 수

        p3.val, carry = add(p1.val, p2.val, carry)  # 먼저 값을 넣어준다
        p1 = p1.next
        p2 = p2.next

        while p1 is not None and p2 is not None: #p3의 next를 연결해준다
            sum, carry = add(p1.val, p2.val, carry)
            p3.next = ListNode(sum)
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next

        if p1 is None: # p3가 먼저 끝났을 경우
            while p2 is not None:
                sum, carry = add(p2.val, 0, carry)
                p3.next = ListNode(sum)
                p3 = p3.next
                p2 = p2.next

        if p2 is None:  # p2가 먼저 끝났을 경우
            while p1 is not None:
                sum, carry = add(p1.val, 0, carry)
                p3.next = ListNode(sum)
                p3 = p3.next
                p1 = p1.next

        if carry != 0:  # carry만 남은경우! 예외처리
            p3.next = ListNode(carry)

        return result


    a = [1,2,3]
    print(functools.reduce(lambda x, y: 10 * x + y, a))
