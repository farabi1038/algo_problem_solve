class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]=='0':
                    continue
                elif i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=min(int(dp[i-1][j]),int(dp[i][j-1]),int(dp[i-1][j-1])) + 1

        return max(max(row) for row in dp)**2
        

        