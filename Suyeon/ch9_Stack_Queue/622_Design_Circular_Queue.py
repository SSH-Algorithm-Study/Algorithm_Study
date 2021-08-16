class MyCircularQueue:

    def __init__(self, k: int):
        self.max = k
        self.front, self.rear = 0, self.max - 1
        self.circular = ['empty'] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():  # 다 찼다면
            return False

        self.rear = (self.rear + 1) % self.max
        self.circular[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.circular[self.front] = "empty"
        self.front = (self.front + 1) % self.max

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.circular[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.circular[self.rear]

    def isEmpty(self) -> bool:
        return self.circular[self.front] == "empty"

    def isFull(self) -> bool:
        return (self.front - self.rear == 1 or self.front - self.rear == -(self.max - 1)) and self.circular[
            self.front] != 'empty'

