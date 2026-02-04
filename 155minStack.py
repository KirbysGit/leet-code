# https://leetcode.com/problems/min-stack/
# medium

class firstAttempt:

    # 02 / 04 / 2026 - 1:47 pm 

    # Runtime -> 391 ms - 5.11%
    # Memory -> 22.55 MB - 30.42%

    # alright so in my head i did this really quick, i was trying to understand
    # like where the struggle in the problem was, but i didn't read that it
    # had to be O(1) time complexity, so i set it up the first way that came to
    # my head.

    # i saw the slow runtime, and realized that the min(self.stack) was O(n)
    # which broke the case most likely causing the slowdown.

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        x = self.stack.pop()
        self.stack.append(x)
        return x

    def getMin(self) -> int:
        return min(self.stack)

class secondAttempt:

    # 02 / 04 / 2026 - 1:48 pm

    # Runtime -> 4 ms - 69.28%
    # Memory -> 22.50 MB - 41.78%

    # the only real change for this was introducing another data structure.
    # idk why i thought you couldn't do this, i thought of that, like maybe
    # some sort of minheap, but i utilized chatgpt just for hints because
    # i couldn't think of a way that would allow me to find the min without
    # a separate data structure.

    # so i set up minStack, which we just add values to if its less than
    # the current min, so the top value is always the minimum value.

    # this is probably the fastest solution, all of the other solutions
    # come out to random times but our peak was the 4 ms but its also the
    # same approach as the 2 ms solution.

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        x = self.stack.pop()
        self.stack.append(x)
        return x

    def getMin(self) -> int:
        return self.minStack[-1]