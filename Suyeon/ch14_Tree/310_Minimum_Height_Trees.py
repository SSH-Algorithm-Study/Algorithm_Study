import collections
import sys

# def findMinHeightTrees( n, edges):
#     info = collections.defaultdict(list)
#     result = collections.defaultdict(list)
#
#     for edge in edges:  # 그래프 연결관계 기록
#         info[edge[0]].append(edge[1])
#         info[edge[1]].append(edge[0])
#
#
#     for i in range(n): # 모든 노드를 한번씩 노드로
#         discovered = []
#         queue = collections.deque()
#         queue.append(i)
#         height = 0
#         while queue:
#             state = 0 # 자식이 발견 됐는지
#             node = queue.popleft()
#             discovered.append(node)
#
#             for child in info[node]:
#                 state
#                 if child not in discovered:
#                     queue.append(child)
#                     state = 1
#
#             if state: # 자식이 하나라도 발견되면 height추가해줘야함
#                 height += 1
#
#         result[height].append(i)
#
#
#     result = sorted(result.items(), key=operator.itemgetter(0)) #작은 값들 node출력  ( Key기준으로 정렬 )
#
#     return result[0]
#
#
#
#
#
#
#
# def findMinHeightTrees( n, edges):
#     info = collections.defaultdict(list)
#     result = collections.defaultdict(list)
#     min_height = sys.maxsize
#
#     for edge in edges:  # 그래프 연결관계 기록
#         info[edge[0]].append(edge[1])
#         info[edge[1]].append(edge[0])
#
#
#     for i in range(n):
#         discovered = []
#         queue = collections.deque()
#         queue.append(i)
#         height = -1
#         while queue:
#             if height > min_height:
#                 break
#             loop = len(queue) #부모만큼 돌기
#             height += 1
#             for _ in range(loop):
#                 node = queue.popleft()
#                 discovered.append(node)
#                 for child in info[node]:
#                     if child not in discovered:
#                         queue.append(child)
#
#         result[height].append(i)
#         min_height = min(min_height, height)
#
#     return result[min_height]


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        info = collections.defaultdict(list)

        for edge in edges:  # 그래프 연결관계 기록
            info[edge[0]].append(edge[1])
            info[edge[1]].append(edge[0])

        leaves = []
        for key in info:
            if len(info[key]) == 1:
                leaves.append(key)

        while n > 2:
            n -= len(leaves)  # 남은 노드 수
            new_leave = []
            for leaf in leaves:
                node = info[leaf].pop()
                info[node].remove(leaf)

                if len(info[node]) == 1:      # 리프소거마다 len체크
                    new_leave.append(node)

            leaves = new_leave

        return leaves




