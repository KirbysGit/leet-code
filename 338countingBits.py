# https://leetcode.com/problems/counting-bits/description/
# easy

class firstAttempt:

    # 11 / 06 / 2025 - 10:04 pm

    # Runtime -> 3 ms - 94.12%
    # Memory -> 18.55 MB - 58.81%

    # alright i sat on this one for a while, trying to break down the patterns.
    # in my head im looking at all the bits listed out and im like okay perfect,
    # the odds have the + 1, the evens dont. but i couldn't figure out how to 
    # find that simple solution i knew there was.

    # i tried with the DP, to understand how the values increment. but my
    # biggest challenge was just to understand how to handle values like 4, 8, 16, 
    # because in my head im like i need to do / 2 then % 2 but that breaks pretty
    # easily, so it was just understanding what we can add from.

    # also i didn't know that // was a thing, i thought that was just for integers
    # but its actually a way to do the floor division which works perfectly with
    # what i needed.

    # looking at the solution : 
    # all we really need to do is understand how to defer the handling of the odd
    # vs the even values. basically what we're doing is we start with our base,
    # which in this case is just an arr with a 0 in it. then we iterate through
    # until n, where we check the odd vs even values. if its odd, we're basically
    # shifting the value to the right by 1 bit then we add 1 to it, because in
    # bits we're basically just dividing it by 2, then flooring it, then we take
    # the value at that index. and then for even values, we do the same thing but
    # don't add the 1. 

    def countBits(self, n: int) -> List[int]:

        arr = [0]
        
        for i in range(1, n + 1):
            if i % 2 == 0:
                arr.append(arr[i // 2])
            else:
                arr.append(arr[i // 2] + 1)

        return arr