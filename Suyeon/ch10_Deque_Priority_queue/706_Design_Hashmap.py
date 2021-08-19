import collections

class ListNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 31
        self.hashtable = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if index in self.hashtable:  # 기존에 있었다면
            p = self.hashtable[index]
            while p:  # 기존 노드의 키들 검사
                if p.key == key:   # 있었다면 덮어쓰기
                    p.value = value
                    return
                p = p.next
            self.hashtable[index] = ListNode(key=key, value= value, next=self.hashtable[index])
        else:  # 기존에 없었다면
            self.hashtable[index] = ListNode(key=key, value=value)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if index in self.hashtable: # index가 차있다면
            p = self.hashtable[index]
            while p: # 돌면서 검사
                if p.key == key:
                    return p.value
                p = p.next

        return -1  # 인덱스 비었거나 key값에 해당되는 노드 없다면

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if index in self.hashtable: # index가 차있다면
            p = self.hashtable[index]
            back = p
            while p: # 돌면서 검사
                if p.key == key:
                    if p == back: # 첫번째 노드이면
                        p = None
                        return
                    back.next = p.next # 중간노드이면 지워주기
                    return
                back, p = p, p.next # 옮겨가기





# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)