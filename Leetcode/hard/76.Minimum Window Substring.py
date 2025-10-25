class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s)==0 or len(t)==0 or len(t)>len(s)):
            return ""

        countT, windows ={},{}
        

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        have, need = 0, len(countT)
        res,resLen=[-1,-1], float("infinity")
        l=0
        for r in range(len(s)):
            c = s[r]
            windows[c] = 1 + windows.get(c,0)

            if c in countT and windows[c]==countT[c]:
                have+=1

            while have ==need:
                if (r-l +1)<resLen:
                    res =[l,r]
                    resLen =(r-l+1)
                windows[s[l]]-=1

                if s[l] in countT and windows[s[l]]<countT[s[l]]:
                    have-=1
                l+=1    
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""
        