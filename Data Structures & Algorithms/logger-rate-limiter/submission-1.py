class Logger:

    def __init__(self):
        self.queue =defaultdict(int)
        


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.queue:
            if timestamp < self.queue[message]:
                return False
        self.queue[message] = timestamp+10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
