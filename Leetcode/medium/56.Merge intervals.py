class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx=0
        intervals.sort()
        for i in range (len(intervals)):
            if idx+1<len(intervals):
                if intervals[idx+1][0]<=intervals[idx][1]:
                   intervals[idx]=[intervals[idx][0],max(intervals[idx+1][1],intervals[idx][1])]
                   intervals.remove(intervals[idx+1])
                else:
                     idx+=1      
        return intervals            

