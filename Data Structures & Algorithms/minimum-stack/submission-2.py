class MinStack:

    def __init__(self):
        self.arr = []
        self.mins = []
        self.size = 0

    def push(self, val: int) -> None:
        
        if self.size == 0 or val < self.getMin():
            self.mins.append(self.size)

        self.arr.append(val)
        self.size += 1

    def pop(self) -> None:

        if self.mins[-1] == self.size - 1:
            del self.mins[-1]

        del self.arr[self.size - 1]
        self.size -= 1 

    def top(self) -> int:
        return self.arr[self.size - 1]

    def getMin(self) -> int:

        return self.arr[self.mins[-1]]
        
