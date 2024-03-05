#minimum character needed for a words

def minimumCharactersForWords(words):
    #wordChar=" ".join(words)
    #wordChar=wordChar.replace(" ","")
    
    hashTable={}
    for i in words:
        currentFreq=freqCount(i)
        maxFreq(currentFreq,hashTable)
        
    
    output= [key for key, value in hashTable.items() for _ in range(value)]        
            
    # Write your code here.
    return output


def maxFreq(current,total):
    for char in current:
        if char in total:
            total[char]=max(current[char],total[char])
        else:
            total[char] =current[char]      
            
def freqCount(words):
    hashTable={}
    for i in words:
        if i not in hashTable:
            hashTable[i]=1
        else:
            hashTable[i]+=1
    return hashTable