#code (longest peak) 845. Longest Mountain in Array (leetcode)
def longestPeak(array):
    # Write your code here.
    longLength =0
    i = 1
    while i<len(array) - 1:
        isPeak = array[i-1] <array[i]  > array[i+1]
        if not isPeak:
            i+=1
            continue
        leftIdx = i -2
        while leftIdx >=0 and array[leftIdx] <array[leftIdx+1]:
            leftIdx -=1
       
        rightIdx = i +2
        while rightIdx <len(array) and array[rightIdx]< array[rightIdx-1]:
            rightIdx +=1
        currentPeakLength =rightIdx -leftIdx -1
        longLength =max(longLength,currentPeakLength)
        i = rightIdx
    return longLength