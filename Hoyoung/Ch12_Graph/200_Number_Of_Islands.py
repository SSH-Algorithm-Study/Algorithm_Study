#처음 푼 풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx=[-1,1,0,0]
        dy=[0,0,1,-1] #왼,오,위,아 4방향 인덱스로 for문 돌기 위해

        def dfs(x,y):
            for i in range(4): #왼,오,위,아
                new_x = x+dx[i]
                new_y = y+dy[i]
                if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]): #인덱스 범위 안 벗어나고
                    if grid[new_x][new_y]=="1" and not visited[new_x][new_y]: #방문한적 없는 1이면
                        visited[new_x][new_y]=True #해당 1 방문처리
                        dfs(new_x,new_y) #해당 1 주변에 인접한 1 들도 모두 방문처리
        
        visited = [[False]*(len(grid[0])) for _ in range(len(grid))] #방문여부 확인용
        
        island_num = 0 #섬의 총수 저장할 변수
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and not visited[i][j]: #방문한적 없는 1이면
                    island_num += 1 #새로운 섬이니 섬의 총수 증가
                    dfs(i,j) #연결되어있는 모든 1 방문 처리
                    
        return island_num