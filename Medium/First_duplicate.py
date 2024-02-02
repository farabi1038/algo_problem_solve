#First_duplicate

def firstDuplicateValue(array):
    # Write your code here.
    s =set()
    for i in array:
        if i in s:
            return i
        else:
            s.add(i)
   
    return -1