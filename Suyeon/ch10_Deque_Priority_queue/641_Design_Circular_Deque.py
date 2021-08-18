class MyCircularDeque:
    class ListNode:
        def __init__(self, val=None, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

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

        if self.isEmpty():  #비여있다면
            self.head = self.tail = self.ListNode(val=value) # head, tail이 같은 곳 가리키게
        else: # 공간이 남았다면
            self.head.left = self.ListNode(val=value, right=self.head) #오른쪽이 head로 new node추가
            self.head = self.head.left # head는 new node로 이동

        self.len += 1

        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """

        if self.isFull():
            return False

        if self.isEmpty():
            self.tail = self.head = self.ListNode(val=value)
        else:
            self.tail.right = self.ListNode(val=value, left=self.tail)  # 왼쪽이 tail인 new node추가
            self.tail = self.tail.right  # tail은 new node로 이동 

        self.len += 1

        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.head = self.head.right

        if self.head is None:  # 마지막 원소를 지웠을 때
            self.tail = None

        else:
            self.head.left = None
        self.len -= 1

        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.tail = self.tail.left

        if self.tail is None:  # 마지막 원소를 지웠을 때
            self.head = None

        else:
            self.tail.right = None

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