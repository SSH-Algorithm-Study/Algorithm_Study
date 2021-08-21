import collections

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.depue()
        self.temp = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.q:
            self.temp.append(self.q.popleft())
        self.q.append(x)
        while self.temp:
            self.q.append(self.temp.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0