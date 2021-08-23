import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid[0])-1
        m = len(grid)/n-1
        queue = collections.deque()

        if grid[0][0] == "1":
            queue.append((0,0))

        while queue:
            x, y = queue.popleft()
            if x >
            if grid[x + 1][y] == "1" and (x + 1, y) not in queue:
                queue.append((x + 1, y))
            if grid[x + 1][y + 1] == "1" and (x + 1, y + 1) not in queue:
                queue.append((x + 1, y + 1))

            if not queue:




