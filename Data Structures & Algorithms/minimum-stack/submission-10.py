class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.min_val = float("inf")


    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.min_val = min(self.minstack[-1],val)
        else:
            self.min_val = val
        self.minstack.append(self.min_val)


    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        x = self.stack[-1]
        return x
        

    def getMin(self) -> int:
        return self.minstack[-1]




        
