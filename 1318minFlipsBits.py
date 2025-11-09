# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# medium

class firstAttempt:

    # 11 / 09 / 2025 - 3:27 pm

    # Runtime -> 42 ms - 20.80%
    # Memory -> 17.87 MB - 32.52%

    # this one had me stumped, like i just didn't understand how to take it incrementally, but
    # you can use the right shift to do that. also like understanding how to handle the bits,
    # becasue its not just a simple OR, we need to handle the other cases, like if there both
    # 1 and 1, and we need a 0, we need to flip both. but the solution is actually much simpler
    
    # ours here takes a bit more general approach to solving, like handling more, but in 
    # reality we only need 4 cases so we are over complicating it here.

    # basically we grab the last bit of each number, then handle if c is 0, then we 
    # have to handle like if both a and b are 1, but if c is 1, we only need to flip one.

    # then we shift the numbers to the right by 1 bit, and repeat the process until we have
    # handled all the bits.

    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            aBit = a & 1
            bBit = b & 1
            cBit = c & 1

            if cBit == 0:
                count += aBit + bBit
            else:
                if (aBit | bBit) == 0:
                    count += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return count

class muchSimpler:
    
    # runtimes are kind of oscillating but i think its around the same
    # speed but much more straight forward, so basically same thing, grab bits,
    # then check the tuples with specific cases, so we can handle that 1 1 0 case
    # as its own thing. 
    
    # but same process other than that.

    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            abit = a%2
            bbit = b%2
            cbit = c%2
            a //= 2
            b //= 2
            c //= 2
            if (abit,bbit,cbit) == (0,0,1):
                count += 1  
            if (abit,bbit,cbit) == (1,0,0): 
                count += 1  
            if (abit,bbit,cbit) == (0,1,0):
                count += 1  
            if (abit,bbit,cbit) == (1,1,0):
                count += 2

        return count