class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for head in lists: # 연결리스트 헤드를 차례대로 받기
            while head:  # 힙에 하나씩 집어넣기 
                heapq.heappush(heap, head.val)
                head = head.next

        result = ListNode() # 결과를 저장할 연결리스트 생성
        p = result

        while heap:  # pop해서 오름차순으로 담기
            p.next = ListNode(heapq.heappop(heap))
            p = p.next

        return result.next