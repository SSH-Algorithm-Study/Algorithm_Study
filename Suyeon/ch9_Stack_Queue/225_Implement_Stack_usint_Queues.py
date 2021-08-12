# class MyStack:
#
#     def __init__(self, val=None, next=None):
#         """
#         Initialize your data structure here.
#         """
#         self.last = None
#         self.val = val
#         self.next = next
#
#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.last = MyStack(x, self.last)
#
#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         value = self.last.val
#         self.last = self.last.next
#
#         return value
#
#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         return self.last.val
#
#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return self.last is None


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0