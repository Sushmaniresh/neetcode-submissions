class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        fresh_fruit = 0 
        mins_passes = 0
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    que.append((r,c,0))
                elif grid[r][c]==1:
                    fresh_fruit+=1
        if fresh_fruit == 0:
            return 0
        while que:
            r,c,mins = que.popleft()
            mins_passed = mins
            directions = [(0,1),(0,-1),(-1,0),(1,0)]
            
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if nr>=0 and nc>=0 and nc<cols and nr<rows and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh_fruit -=1
                    que.append((nr,nc,mins+1))
        return mins_passed if fresh_fruit == 0 else -1
                    





