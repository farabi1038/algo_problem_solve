#reverse string keeping the words same


def reverseWordsInString(string):
    # Write your code here.
    stringR = string[::-1]
    output=[]
    l=r=len(string)-1
    for i in range(len(string)):
        if string[l]!=' ':
            l-=1
        else:
            output.append(string[l+1:r+1])
            l=r=l-1
            
    output.append(string[l+1:r+1])        
    return " ".join(output)
