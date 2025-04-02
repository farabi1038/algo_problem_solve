class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num_iter= ''
        i,j=0,0
        while i<len(word) and j<len(abbr):
            if abbr[j].isdigit():
                if abbr[j]=='0':
                    return False
                num_iter= ''
                while j<len(abbr) and abbr[j].isdigit():
                    num_iter+=abbr[j]
                    j+=1
                i+=int(num_iter)        
            else:
                if i>=len(word) or word[i]!=abbr[j]:
                    return False
                i+=1
                j+=1 
        return i==len(word) and j==len(abbr)           
                                                  

        