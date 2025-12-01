# https://leetcode.com/problems/insert-delete-getrandom-o1/
# medium

class firstAttempt:

    # 12 / 01 / 2025 - 12:05 pm

    # Runtime -> 358 ms - 5.12%
    # Memory -> 57.67 MB - 86.10%

    # i mean moving through it its pretty simple, just how do we insert, remove, and get random in O(1) time?
    # i actually didn't even realize it wanted us to do it in O(1) time, so i just did it how i thought,
    # so now i gotta try this again avoiding O(n).

    def __init__(self):
        self.randomSet = []

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomSet.append(val)
            return True
    
    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.randomSet)
        
class better:

    # 12 / 01 / 2025 - 12:10 pm

    # Runtime -> 86 ms - 97.78%
    # Memory -> 57.22 MB - 97.67%

    # alright so with o(1), pretty simple idea but definitely weird to look at without
    # immediately getting how it needs to be o(1). but anyways, idea is to use a dictionary
    # to keep track of the positions of the values in the list where the value is the key, and
    # the position is the value. while still using another array for the actual values.

    # so basically we just need to keep track of the positions of the values in the list on
    # top of what we were doing prior as well as use those positions during the insert and
    # remove operations.

    # in insert all we do it take the len of the array and set the value to the index at that
    # spot, and then we know where the index is in the "set".

    # in delete we have to do a bit more, obviously first initial check if its in it,
    # then if it is, we need to do a swap with wherever the val is and the last index,
    # this will allow us to pop from the top, and easily delete the key from the pos
    # dict. 

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.arr)
        self.arr.append(val)

        return True

    def delete(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        self.arr[idx] = last
        self.pos[last] = idx

        self.arr.pop()
        del self.pos[val]

        return True
    
    def getRandom(self) -> int:
        return random.choice(self.arr)
    