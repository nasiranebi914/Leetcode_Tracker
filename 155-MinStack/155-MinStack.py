# Last updated: 6/17/2025, 10:34:58 PM
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = val if not self.minimum else min(val, self.minimum[-1])
        self.minimum.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()      

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()