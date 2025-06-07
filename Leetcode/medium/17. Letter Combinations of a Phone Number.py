class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res=[]
        if len(digits)==0:
            return res
        self.dfs(digits,0,dic,'',res)
        return res
    def dfs(self,nums,idx,dic,path,res):
        if idx>=len(nums):
            res.append(path)
            return
        str1=dic[nums[idx]]
        for i in str1:
            self.dfs(nums,idx+1,dic,path+i,res)        
        