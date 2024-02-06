
#merge overalpping interval


def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort()
    #print(intervals)
    idx=0
    for i in range (len(intervals)):
        if(idx+1<len(intervals)):
           
            if(intervals[idx][1]>=intervals[idx+1][0]):
                if (intervals[idx][1]>=intervals[idx+1][1]):
                    intervals[idx]=[intervals[idx][0],intervals[idx][1]]
                    intervals.remove(intervals[idx+1])    
                else:
                   
                    intervals[idx]=[intervals[idx][0],intervals[idx+1][1]]
                    intervals.remove(intervals[idx+1])
                    #print(intervals)
            else:
                idx+=1
    #print(intervals)    
    return intervals


#or



def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort()
    #print(intervals)
    idx=0
    for i in range (len(intervals)):
        if(idx+1<len(intervals)):
           
            if(intervals[idx][1]>=intervals[idx+1][0]):
                    intervals[idx]=[intervals[idx][0],max(intervals[idx][1],intervals[idx+1][1])]
                    intervals.remove(intervals[idx+1])  
                    #print(intervals)
            else:
                idx+=1
    #print(intervals)    
    return intervals



#or Node approach :

class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second

def merge_intervals(v):
  idx=0
  v.sort(key=lambda x: x.first)
  # write your code here
  for i in range(len(v)):
    if idx+1<len(v):
      if v[idx].second >=v[idx+1].first:
        v[idx]=Pair(v[idx].first,max(v[idx+1].second,v[idx].second))
        v.remove(v[idx+1])
      else:
        idx+=1    
        
  return v
