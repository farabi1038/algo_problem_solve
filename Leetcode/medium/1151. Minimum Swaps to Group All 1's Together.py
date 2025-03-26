class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num_ones= sum(data)
        n = len(data)
        swap=0
        if num_ones==0 or num_ones== len(data):
            return 0

        curr_ones = sum(data[:num_ones])
        swap = num_ones - curr_ones    
        for i in range(1,n- num_ones+1):
            curr_ones = curr_ones -data[i-1]+data[num_ones+i-1]
            swap =min(swap,num_ones-curr_ones)
        return swap    


#data = [1, 0, 1, 0, 1, 0, 0, 1] , i=0, [1,0,1,0]
#i=1, [0,1,0,1]
        