#longest palindrome check


def longestPalindromicSubstring(string):
    # Write your code here.
    current_long=[0,1]
    for i in range (1,len(string)):
        odd =get_long(string,i-1,i+1)
        even=get_long(string,i-1,i)
        longest= max(odd,even,key = lambda x:x[1]-x[0])
        current_long=max(current_long,longest,key= lambda x:x[1]-x[0])
    return string[current_long[0]:current_long[1]]
        
       
def get_long(string,sIdx,eIdx):
    #print(sIdx,eIdx,len(string))
    while sIdx>=0 and eIdx<len(string):
       
        if string[sIdx]!=string[eIdx]:
            break
        sIdx-=1
        eIdx +=1
    return [sIdx+1,eIdx]
        
#abaxyzzyxf