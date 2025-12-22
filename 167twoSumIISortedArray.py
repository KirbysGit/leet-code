# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# medium

class firstAttempt: 

    # 12 / 22 / 2025 - 3:00 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 18.54 MB - 57.39%

    # went through a bunch of ideas for this one,
    # first off tried to set it up where like we do the pointers in the middle working
    # outwards, then i realized that didn't really work because we would never pass 
    # some of the solutions.
    # then wanted to just do them both starting at the front, like 0 and 1, but 
    # with some cases it takes too long.
    # then i tried like one at front and one at end, and it worked out perfectly!

    # so the idea is start one at front and one at end, and if the added value is
    # less than target, move front ptr up, and if added value is greater than target
    # move back ptr down.

    # no gpt! im the goat!!

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        ptr1 = 0
        ptr2 = n - 1

        while(1):
            added = numbers[ptr1] + numbers[ptr2]
            if added == target:
                return [ptr1 + 1, ptr2 + 1]
            elif added < target:
                ptr1 += 1
            else:
                ptr2 -= 1

        