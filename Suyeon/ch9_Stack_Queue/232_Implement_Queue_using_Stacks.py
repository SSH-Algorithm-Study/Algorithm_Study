class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        self.peek()

        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """

        if len(self.stack2) == 0:
            while len(self.stack1) != 0:  # stack1에 있는것 다 가져와서 거꾸로 넣기
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return len(self.stack1) == 0 and len(self.stack2) == 0