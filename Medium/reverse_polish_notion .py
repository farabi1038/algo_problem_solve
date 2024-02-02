#reverse_polish_notion or post fix equation calculation:

def reversePolishNotation(tokens):
    # Write your code here.
    stack=[]
    stack.append(tokens[0])
    idx=1
    result=0
    while len(stack)>0 and idx<len(tokens):
        if tokens[idx] in "+-*/":
            top1=stack.pop()
            top2=stack.pop()
            if tokens[idx]=='+':
                result=int(top1)+int(top2)
                stack.append(result)
            if tokens[idx]=='-':
                result=int(top2)-int(top1)
                stack.append(result)
            if tokens[idx]=='*':
                result=int(top1)*int(top2)
                stack.append(result)
            if tokens[idx]=='/' and int(top1)!=0:
                result=int(int(top2)/int(top1))
                stack.append(result)
        else:
            stack.append(tokens[idx])
        idx+=1
    return int(stack.pop()) if len(stack)!=0 else result
