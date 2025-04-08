class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length=0

        if grid[0][0]==0:
            q=deque([[0,0,1]]) 
        else:
            return -1
        visited =set()

        nei =[[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]
        while q:
            x,y,dist = q.popleft()
            if (x,y)==(len(grid)-1,len(grid)-1): return dist
            for dx,dy in nei:
                if 0<=x+dx<len(grid) and 0<=y+dy<len(grid) and grid[x+dx][y+dy]==0 and (x+dx,y+dy) not in visited:
                    visited.add((x+dx,y+dy))
                    q.append([x+dx,y+dy,dist+1])
        return -1               
        