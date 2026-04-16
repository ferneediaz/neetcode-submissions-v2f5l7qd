class MinStack:

    def __init__(self):
        self.MinStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MinStack:
            self.MinStack.append(val)
        elif self.MinStack[-1] >= val:
            self.MinStack.append(val)
            


    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.MinStack[-1]:
            self.MinStack.pop()
            
    def top(self) -> int:
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.MinStack[-1]
