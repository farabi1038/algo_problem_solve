#Balancing brakets


def balancedBrackets(string):
    # Write your code here.
    stack=[]
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    for i in range(len(string)):
        if string[i]=='(' or string[i]=='{' or string[i]=='[':
            stack.append(string[i])
        elif string[i]==')' or string[i]=='}' or string[i]==']':
            if len(stack)==0 or stack[-1] != bracket_pairs[string[i]]:
                return False
            stack.pop()
    if len(stack)==0:
        return True
    return False    