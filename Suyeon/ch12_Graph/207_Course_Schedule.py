
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pairs = collections.defaultdict(list)

        for prerequisite in prerequisites:  # key값이 완료되면 수행가는한 value들
            pairs[prerequisite[1]].append(prerequisite[0])

        unvisited = 0
        processing = 1
        processed = 2

        visit = [unvisited] * numCourses # 방문여부

        def dfs(i):
            if visit[i] == processing:  # 진행중인 노드
                return False

            if visit[i] == processed:  # 이미 탐색을 맞힌 노드
                return True

            visit[i] = processing
            for child in pairs[i]: # 이웃노드들 방문
                if not dfs(child):
                    return False

            visit[i] = processed
            return True



        for i in range(numCourses):  #0 - n-1 노드 차례대로
            if not dfs(i):
                return False

        return True



