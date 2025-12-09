# https://leetcode.com/problems/roman-to-integer/
# easy

class firstAttempt:

    # 7 ms. 

    def romanToInt(self, s: str) -> int:
        
        chars = list(s)
        chars.reverse()

        amount = 0
        lastLtr = None
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for ltr in chars:
            val = roman.get(ltr)
            if ltr == 'I' and (lastLtr == 'V' or lastLtr == 'X'):
                amount -= 1
            elif ltr == 'X' and (lastLtr == 'L' or lastLtr == 'C'):
                amount -= 10
            elif ltr == 'C' and (lastLtr == 'D' or lastLtr == 'M'):
                amount -= 100
            else:
                amount += val

            lastLtr = ltr

        return amount

class tryingToNotReverse:

    # 5 ms.

    def romanToInt(self, s: str) -> int:
        
        n = len(s)
        chars = list(s)
        chars.append(0)

        amount = 0
        ltr = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while ltr < n:
            val = roman.get(chars[ltr])
            if ltr != n - 1:
                nxtLtr = roman.get(chars[ltr + 1])
            else:
                nxtLtr = 0
                
            if val < nxtLtr:
                amount -= val
            else:
                amount += val
            
            ltr += 1

        return amount

class gptHint:

    # 5 ms.

    # similar approach to last one but much cleaner, main thing is in checking (i + 1 < n), thats
    # where i was going wrong a bit.

    def romanToInt(self, s: str) -> int:
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        amount = 0

        for i in range(n):
            if i + 1 < n and roman[s[i]] < roman[s[i+1]]:
                amount -= roman[s[i]]
            else:
                amount += roman[s[i]]
            
        return amount