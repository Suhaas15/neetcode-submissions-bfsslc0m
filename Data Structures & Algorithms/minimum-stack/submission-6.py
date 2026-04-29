class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp=[]
        minNum = float('inf')

        while self.stack:
            minNum = min(minNum, self.stack[-1])
            temp.append(self.stack.pop())
        
        while temp:
            self.stack.append(temp.pop())
        
        return minNum
