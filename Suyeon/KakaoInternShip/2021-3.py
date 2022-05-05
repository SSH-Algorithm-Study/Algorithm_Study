class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev



def solution(n, k, cmd):
    answer = ''

    # 초기화
    head = Node(-1)
    p = head
    cur = None
    for i in range(n):
        p.next = Node(i,p)
        p = p.next
        if k == i:
            cur = p

    head.prev = p
    p.next = head



    # 실행
    delete = []

    for c in cmd:
        c = c.split()
        # 위로 이동
        if c[0] == "U":
            interval = int(c[1])
            for i in range(interval):
                cur = cur.prev

        # 아래로 이동
        elif c[0] == "D":
            interval = int(c[1])
            for i in range(interval):
                cur = cur.next

        # 지우기
        elif c[0] == "C":
            delete.append(cur)
            if head.prev == cur: # 마지막이면
                cur.prev.next, cur.next.prev, cur = cur.next, cur.prev, cur.prev
            else: # 아니면
                cur.prev.next, cur.next.prev, cur = cur.next, cur.prev, cur.next

        # 복구
        else:
            z_node = delete.pop()
            z_node.prev.next, z_node.next.prev = z_node, z_node


    # 비교
    answer = ["X"] * n

    p = head.next
    for _ in range(n):
        answer[p.val] = "O"
        p = p.next


    return "".join(answer)


print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))