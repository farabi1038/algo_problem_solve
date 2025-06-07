class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        # @lru_cache(None)
        def dfs(i,t_list,total):
            if total>target or len(candidates)==i :
                return
            
            if total ==target:
                res.append(t_list)
                return
           
            dfs(i,t_list+[candidates[i]],total+candidates[i])
            dfs(i+1,t_list,total)
        dfs(0,[],0)
        return res            
        