#one edit to make two string same


def oneEdit(stringOne, stringTwo):
    index1=0
    index2=0
    len1=len(stringOne)
    len2=len(stringTwo)
    edit=False
    if abs(len1-len2)>1:
        return False
    while index1<len1 and index2<len2:
        if stringOne[index1]!=stringTwo[index2]:
            
            if edit:
                return False
            edit=True
            
            if len1>len2:
                index1+=1
                continue
    
            if len2>len1:
                index2+=1
            else:
                index1+=1
                index2+=1
        else:
            index1+=1
            index2+=1    
    if index1 < len1 or index2 < len2:
        if edit:
            return False          

    return True
print(oneEdit("bb", "a"))