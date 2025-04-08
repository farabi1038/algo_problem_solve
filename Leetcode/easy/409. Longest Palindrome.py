class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=Counter(s)
        odd=False
        val=0

        for i in count.values():
            if i%2==0:
                val+=i
            else:
                val+=(i-1)
                odd= True
        return 1+ val if odd else val        

        