import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
             list = []
             while head!= None:
                list.append(head.val)
                head = head.next

             if list == list[::-1]:
                 return True
             else:
                 return False


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        deque = collections.deque

        while head != None:
            deque.append(head.val)
            head = head.next

        while deque:
            if deque.pop() != deque.popleft():
                return False

        return True


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list = []

        if head is None:
            return True

        while head != None:
            list.append(head.val)
            head = head.next

        while len(list) > 1:
            if list.pop(0) != list.pop():
                return False

        return True

#deque.reverse()는 inplace 정렬이다
#리스트에서 Pop(1) o(n)이다


node = ListNode(3,ListNode(2))
node2= ListNode(7)

print(id(node))
rev, rev.next, node = node, node2, node.next

print(id(rev), id(node), id(rev.next), rev.next.val, node.val)




