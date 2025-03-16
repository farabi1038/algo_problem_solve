class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        

        def backTrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range (start, len(candidates)):
                if candidates[i]>target:
                    continue
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                    
                backTrack(i+1, target-candidates[i],path+[candidates[i]])
        backTrack(0,target,[])
        return result