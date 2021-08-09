# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 빈 입력에 대한 예외처리
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        p1 = l1
        p2 = l2
        root = ListNode()  # 두 연결리스트를 합칠 새로운 리스
        p3 = root

        if p1.val <= p2.val:
            p3.val = p1.val
            p1 = p1.next

        else:
            p3.val = p2.val
            p2 = p2.next

        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next  # p1 다음으로 옮기기
            else:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next  # p2 다음으로 옮기기

        # 둘중하나라도 끝에 도달했다면 나머지 옮기기
        if p1 == None:
            while p2 != None:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next

        if p2 == None:
            while p1 != None:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next

        return root