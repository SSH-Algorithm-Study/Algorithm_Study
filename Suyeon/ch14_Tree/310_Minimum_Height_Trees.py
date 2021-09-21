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
#     for i in range(n):
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







def findMinHeightTrees( n, edges):
    info = collections.defaultdict(list)
    result = collections.defaultdict(list)
    min_height = sys.maxsize

    for edge in edges:  # 그래프 연결관계 기록
        info[edge[0]].append(edge[1])
        info[edge[1]].append(edge[0])


    for i in range(n):
        discovered = []
        queue = collections.deque()
        queue.append(i)
        height = -1
        while queue:
            if height > min_height:
                break
            loop = len(queue) #부모만큼 돌기
            height += 1
            for _ in range(loop):
                node = queue.popleft()
                discovered.append(node)
                for child in info[node]:
                    if child not in discovered:
                        queue.append(child)

        result[height].append(i)
        min_height = min(min_height, height)

    return result[min_height]


print(findMinHeightTrees( 6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))


