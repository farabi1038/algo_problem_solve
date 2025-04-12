class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid :
            return 0
        row,col =len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c]!='1':
                return 
            grid[r][c]='#'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        island=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(i,j)
                    island+=1
        return island            

        