# https://leetcode.com/problems/h-index/
# medium

class firstAttempt:

    # 11 / 30 / 2025 - 8:04 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 18.03 MB - 62.90%

    # this one was honestly a struggle, idk if i would've found the approach i saw on wikipedia on
    # my own. but basically, it references the wikipedia page for h-index, and it gives you the 
    # formula to solve for it. but its pretty vague, so i had to use chatgpt help me understand 
    # where i was going wrong. 
    
    # the article brought up sorting and reversing the array, so like from greatest to least.
    # then from there, we iterate through, and per index we are checking to see if the value at
    # that index is less than the idx + 1, if so we return the idx.
    
    # basically, because we're sorting from greatest to least, the first index that satisfies the condition
    # will be the h-index, considering it doesn't break on the other cases like if n is equal to 1.

    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        citations.sort()
        citations.reverse()
        avg = 1

        for idx in range(0, n):
            if citations[idx] < idx + 1:
                return idx

        if n == 1:
            if citations[0] > 0:
                return avg
            else:
                return 0

        return n
    
class cleanerCode:

    # way simpler to look at, but pretty much the same, just handles the other cases way
    # better. 
    
    # start off, say fuck it on the reverse sort because its not really needed thats just a condition reverse.
    # but then as we iterate through, we check to see if the length - idx is less than or equal to the value at that
    # index, because it means that the number of citations is greater than equal to index + 1.

    # then we return the length - idx, because that will be the h-index.

    def hIndex(self, citations: List[int]) -> int:

        length = len(citations)
        citations.sort()

        for idx, value in enumerate(citations):
            if length - idx <= value:
                return length - idx

        return 0