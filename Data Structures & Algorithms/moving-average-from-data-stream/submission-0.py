from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.numbers = deque(maxlen=size)
        self.left = 0
        self.right = 0
        

    def next(self, val: int) -> float:
        self.numbers.append(val)
        new_average = 0
        for n in self.numbers:
            new_average += n



        return new_average / len(self.numbers)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
