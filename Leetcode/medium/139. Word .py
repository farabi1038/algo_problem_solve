class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        wordSet=set(wordDict)
        memo ={}

        def dp(start):
            if start==n:
                return True
            if start in memo:
                return memo[start]
            for end in range(start+1,n+1):
                word =s[start:end]
                if word in wordSet and dp(end):
                    memo[start]=True
                    return True
            memo[start] = False
            return False

        return dp(0)                