# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head,  left, right):
        if left == right:
            return head

        p = head
        list = []

        while p is not None:  # list에 옮기기
            list.append(p.val)
            p = p.next

        if right == len(list):
            list = list[:left - 1] + list[right - 1:left - 2:-1]
        else:
            list = list[:left - 1] + list[right - 1:left - 2:-1] + list[right:]  # 중간에 범위만큼 반전

        result = ListNode(list[0])
        p = result

        for i in range(1, len(list)):
            p.next = ListNode(list[i])
            p = p.next

        return result


# range, 슬라이싱 문법 차이



print(list(range(2,-1,-1)))