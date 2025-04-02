class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1

        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                a1,b1=i,j-1
                a2,b2=i+1,j
                flag=True
                while a1<b1:
                    if s[a1]!=s[b1]:
                        flag=False
                        break
                    a1+=1
                    b1-=1 
                if flag : return True       
                while a2<b2:
                    if s[a2]!=s[b2]:
                        return False
                    a2+=1
                    b2-=1    
                return True
                
        return True
        