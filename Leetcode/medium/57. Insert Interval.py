class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx = 0
        intervals.sort()
        while idx + 1 < len(intervals):
            if intervals[idx + 1][0] <= intervals[idx][1]:
                intervals[idx] = [intervals[idx][0], max(intervals[idx + 1][1], intervals[idx][1])]
                intervals.pop(idx + 1)
            else:
                idx += 1
        return intervals

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals) 
        