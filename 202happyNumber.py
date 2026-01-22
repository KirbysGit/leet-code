# https://leetcode.com/problems/happy-number/description/
# easy

class firstAttempt:

    # 01 / 22 / 2026 - 1:09 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.46 MB - 7.40%

    # alright i took a minute for this one, just to think through, like i was so confused on
    # how i could approach it without literally trying every possible combination, i wasn't
    # really understanding where there could be a breakcase for me to use. 

    # but while i was cooking up brekky i was drawing the pattern out with the value "12" as
    # the starting number and noticed how it began to loop if you go long enough, so to prevent
    # that loop if i just had some sort of list to keep track of the numbers i've seen, i could
    # just return false and it would save a ton of time.

    # so i did that! except i used a set because i've learned better and also removing duplicates 
    # doesn't actually matter in this scenario.

    def isHappy(self, n: int) -> bool:

        seen = set()
        total = n

        while (1):
            cur = 0
            for digit in str(total):
                cur += int(digit) * int(digit)
            
            if cur == 1:
                return True
            elif cur in seen:
                return False
            else:
                seen.add(cur)
                total = cur

    