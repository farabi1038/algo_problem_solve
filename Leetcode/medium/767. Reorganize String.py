from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        count_max, count_freq = max(count.items(),key=lambda c:c[1])
        if (count_freq)>(len(s)+1)//2:
            return ""

        res=[""]*len(s)
        i=0
        for _ in range(count_freq):
            res[i]=  count_max
            i=i+2
        count[count_max] =0

        for char,freq in count.items():
            for _ in range(freq):
                
                if i>=len(s):
                    i=1
                res[i]=char
                i=i+2      
        return "".join(res)            
        
