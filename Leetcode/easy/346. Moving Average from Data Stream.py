class MovingAverage:

    def __init__(self, size: int):
        self.num =[]
        self.size=size

        

    def next(self, val: int) -> float:
        self.num.append(val)
        if len(self.num)>self.size:
            self.num.pop(0)
        return sum(self.num)/len(self.num)    


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)