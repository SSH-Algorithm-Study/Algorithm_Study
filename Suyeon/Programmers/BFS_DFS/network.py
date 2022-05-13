def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i, visit in enumerate(visited):
        if not visit: # 방문안한 곳만
            queue = [i]
            visited[i] = True # 방문표시
            while queue:
                child = queue.pop(0)
                for i, connect in enumerate(computers[child]):
                    if connect and i != child and not visited[i]: # 연결되어있고 방문안했으며 자신과 같지않은
                        queue.append(i)
                        visited[i] = True # 바로바로 방문기록
            answer += 1

    return answer


