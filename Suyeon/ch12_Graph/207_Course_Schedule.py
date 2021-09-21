import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pairs = collections.defaultdict(list)

        for prerequisite in prerequisites:  # key값이 완료되면 수행가는한 value들
            pairs[prerequisite[1]].append(prerequisites[0])

        leave = list(range(numCourses))
        result = False

        def dfs(start, discovered):
            nonlocal result
            if result:
                return
            if start in discovered: # 이미 있는경우 뒤로 돌아가기
                return
            if len(discovered) == numCourses:  # 가능한 경로로 다 찾았을 경우 True 바꾸기
                result = True
                return

            for next in pairs[start]:
                dfs(next, discovered+[start])


        for i in range(numCourses):
            dfs(i,[])
            if result:
                return True


