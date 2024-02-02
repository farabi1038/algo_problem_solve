#sort the stack using recursion only


def sortStack(stack):
    # Write your code here.
     if len(stack)==0:
        return stack
     top = stack.pop()
     sortStack(stack)
     sort(stack,top)
     return stack
def sort(stack,value):
    if len(stack)==0 or stack[len(stack)-1]<=value:
        stack.append(value)
        return
    top= stack.pop()

    sort(stack,value)
    stack.append(top)
