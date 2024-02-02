
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
