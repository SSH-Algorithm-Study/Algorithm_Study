N, M = map(int,input().split())
result = []

def dfs(start,n):
    if n == M:
        print(*result)
        return

    for num in range(start,N+1):
        result.append(num)
        dfs(num,n+1)
        result.pop()

dfs(1,0)