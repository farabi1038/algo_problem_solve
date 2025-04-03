class Solution:
    def simplifyPath(self, path: str) -> str:
        direct = path.split('/')
        stack = deque()
        for dir in direct:
            if dir =='.' or not dir:
                continue
            elif dir =='..':
                if stack :
                    stack.pop()
            else:
                stack.append(dir)   

        return '/'+'/'.join(stack)                 
        