#next greater element

def nextGreaterElement(array):
    # Write your code here.
    res=[-1]*len(array)
    stack=[]
    stack.append(0)
    for i in range(2*len(array)):
        while len(stack)>0 and array[i%len(array)]>array[stack[-1]]:
            top=stack.pop()
            res[top]=array[i%len(array)]
        stack.append(i%len(array))    
    return res
