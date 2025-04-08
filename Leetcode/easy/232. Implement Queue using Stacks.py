class MyQueue:

    def __init__(self):
        self.stack_in =[]
        self.stack_out =[]
        

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.move()
        value =self.stack_out.pop()
        return value
        

    def peek(self) -> int:
        self.move()
        return self.stack_out[-1]
    def move(self):
         
        if not  self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()