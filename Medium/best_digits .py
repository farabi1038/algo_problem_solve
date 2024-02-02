#Finding best digits to remove based on numDigits so that number is being enough 

def bestDigits(number, numDigits):
    # Write your code here.
    stack=[]
    numD=numDigits
    for i in number:
            while len(stack)>0 and numD>0 and int(i)>int(stack[-1]):
                stack.pop()
                numD-=1
            stack.append(i)
        
    while numD>0:
        stack.pop()
        numD-=1
        
            
    return "".join(stack)
