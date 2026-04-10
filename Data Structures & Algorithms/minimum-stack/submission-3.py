class MinStack:

    def __init__(self):
        self.arr = []
        self.minStack = []

        #we have two stacks. 
        #the minstack keeping record of the minimum at each point
        #

    def push(self, val: int) -> None:
        self.arr.append(val)
        #i only want to add the minimum number to the back of my min stack only. 
        #so when its time to pop from the end i always give you the min
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)


    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
