# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head,  left, right):
        # p : Rev의 head , q : p의 다음원소 , link1: left바로 전으로 나중에 이어줄 왼쪽 , link2 : left로 나중에 이어줄 오른쪽
        #p,link1구하기
        if left == 1:  # 첫 인덱스부터 시작할 때
            p = head   # 바로 p가 head
            link1 = None  # link1은 없음
        else:
            link1 = head    #link1은 head에서 시작
            for _ in range(left-2):  # 반전할 지점 바로 전까지 link1옮겨주기
                link1 = link1.next
            p = link1.next   # 다 옮겼다면 p는 left값

        #link2, q설정
        link2 = p   # link2 저장
        q= p.next   # q는 p바로다음


        # q하나씩 가져와서 p앞에 붙이고 p는 rev의 헤드유지
        for _ in range(right - left):
            p, q.next , q = q, p, q.next

        #이어주기
        if link1:  #link1이 있다면 이어주기
            link1.next = p
        if not link1: #link1없다면 head를 p로
            head = p

        link2.next = q   # link2이어주기


        return head



class Solution:
    def reverseBetween(self, head,  left, right):

        root = start = ListNode(None)
        root.next = head

        for _ in range(left-1):
            start = start.next

        end = start.next

        for _ in range(right - left):
            start.next, end.next.next, end.next = end.next, start.next, end.next.next

        return root.next




        else:
            link1 = head    #link1은 head에서 시작
            for _ in range(left-2):  # 반전할 지점 바로 전까지 link1옮겨주기
                link1 = link1.next
            p = link1.next   # 다 옮겼다면 p는 left값

        #link2, q설정
        link2 = p   # link2 저장
        q= p.next   # q는 p바로다음


        # q하나씩 가져와서 p앞에 붙이고 p는 rev의 헤드유지
        for _ in range(right - left):
            p, q.next , q = q, p, q.next

        #이어주기
        if link1:  #link1이 있다면 이어주기
            link1.next = p
        if not link1: #link1없다면 head를 p로
            head = p

        link2.next = q   # link2이어주기


        return head
