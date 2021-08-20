class ListNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = self.tail = None
        self.max = k
        self.len = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty(): # 비었을 때
            self.head = self.tail = ListNode(val=value)

        else:  # 아닐 때
            self.head.left = ListNode(val=value, right = self.head) # 새로운 노드의 오른쪽은 헤드
            self.head = self.head.left  # 기존헤드 옮기기
        self.head.left = self.tail
        self.tail.right = self.head


        self.len += 1

        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """

        if self.isFull():
            return False

        if self.isEmpty():  # 비었을 때
            self.head = self.tail = ListNode(val=value)

        else:  # 아닐 때
            self.tail.right = ListNode(val=value, left=self.tail)  # 새로운 노드의 왼쪽은 테일
            self.tail = self.tail.right  # 기존테일 옮기기

        self.head.left = self.tail
        self.tail.right = self.head
        self.len += 1

        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.right
            self.head.left = self.tail
            self.tail.right = self.head

        self.len -= 1

        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.left
            self.head.left = self.tail
            self.tail.right = self.head

        self.len -= 1

        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.head.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """

        # return self.head is None and self.tail is None
        return self.len == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        # p = self.head
        #
        # for _ in range(self.max):
        #     if p is None:
        #         return False
        #     p = p.right
        #
        # return True
        return self.len == self.max



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()