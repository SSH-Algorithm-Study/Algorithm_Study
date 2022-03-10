######## 정렬함수

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

for num in nums:
    print(num)

############## 삽입정렬

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

root = Node(-10000)

for _ in range(N):
    num = int(input())
    bef = root
    cur = root

    while cur and cur.val < num:
        bef = cur
        cur = cur.next

    bef.next = Node(num, bef.next)


while root.next:
    print(root.next.val)
    root = root.next