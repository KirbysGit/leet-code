# https://leetcode.com/problems/smallest-number-in-infinite-set/
# medium

class firstAttempt:

    # 10 / 20 / 2025 - 1:09 pm

    # Runtime -> 14 ms - 79.83%
    # Memory -> 18.50 MB - 32.02%

    # had to use chatgpt for syntax for dictionary. 
    # but i wrote out my idea for how i was going to do it and how
    # i communicated it to chatgpt which ill put below.
    
    # but like i understood how i felt we needed to do it
    # but i didn't really understand how to properly reference the 
    # newest value, also handling the pop operation on the addedback
    # values.

    # the problem is spread across three parts.
    # first off with the __init__, i knew using an actual large set
    # would be fucking stupid, so instead just keeping track of the last
    # value we added with an incrementing int. and also keeping track
    # of the added values in an array only if its less than that value.

    # secondly, with the popSmallest(), i knew we needed to check if 
    # the array existed, and if the current value of the addBack array
    # was smaller than the last value we added so we have the initial check
    # for that, else just take the cur value, then increment it.

    # thirdly, for addBack(), we need to check if its less than the
    # last value we added, if so we add it to the array, and we don't need
    # to check for duplicates because we use a set.

    class SmallestInfiniteSet:

    # my initial idea below below :

    # alright so my idea not really knowing how to approach this problem
    # is to first initialize a set. 

    # im thinking that an true "infinite" set would be too much time
    # and memory to actually set up, so we instead "simulate" it by
    # just keeping track of the values that have been added, like maybe
    # start it out with just 1, but we can then know that if they are
    # adding back 2, its in there if we have just a 1, because it looks
    # like the set exists in increasing order.

    # but for popSmallest, we take whichever one we have, like a 1, 
    # then take it out, and just have its next character in it like increment
    # the 1 + 1 so thats the next char to come out.

    # then with add back we handle it like if its greater infSet[0] then
    # do nothing because we can assume its in there, and then if
    # its not greater then add that to like the first value ahead of our
    # only other initial value then output that at the next popSmallest.

    def __init__(self):
        self.cur = 1
        self.addedBack = set()

    def popSmallest(self) -> int:
        if self.addedBack and min(self.addedBack) < self.cur:
            smallest = min(self.addedBack)
            self.addedBack.remove(smallest)
            return smallest

        val = self.cur
        self.cur += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.cur:
            self.addedBack.add(num)


class fasterWithHeap:

    # Runtime -> 9ms - 92.86%
    # Memory -> 18.42 MB - 53.02%

    # chatgpt suggested using a heap rather than a set, but its approach
    # was ineffficient so i saw this one on the solutions tab.

    # the main difference is using a heap to keep track of the addedback values.

    # so replaced = [] is a head, and counter is just the cur value.

    # then if replaced is not empty, we pop smallest value from it.

    # for add back, same logic as our other solution just referencing a heap instead of the set.

    def __init__(self):
        self.replaced = []
        self.counter = 1 

    def popSmallest(self) -> int:
        if self.replaced:
            return heapq.heappop(self.replaced)
        smallest = self.counter
        self.counter += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.counter and num not in self.replaced:
            heapq.heappush(self.replaced, num)