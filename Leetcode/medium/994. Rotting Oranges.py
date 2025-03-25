from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        q =deque()
        fresh =0
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,time))
                if grid[i][j]==1:
                    fresh+=1    

        if fresh==0:
            return 0


        while q:
            x,y,time =q.popleft()
            for i,j in directions:
                if 0<=x+i<len(grid) and 0<=y+j<len(grid[0]) and grid[x+i][y+j]==1:
                    grid[x+i][y+j]=2
                    fresh-=1
                    q.append((x+i,y+j,time+1))
        return time if fresh==0 else -1            





        