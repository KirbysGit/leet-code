# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# easy

class firstAttempt:
    # 09 / 04 / 2025 - 2:30pm

    # Runtime -> 0ms - 100.00%
    # Memory -> 17.95 MB - 26.58%

    # basic check at start for case that them summed are not equal
    # then use gcd of lengths to get substring, if gcd is 0 return empty string
    # find if substring is equal to str1 and str2 multiplied by their multipler
    # if so return substring, else return empty string

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 != str2 + str1):
            return ""
        
        m, n = len(str1), len(str2)

        g = gcd(m, n)

        if (g == 0):
            return ""

        div = str1[:g]
        
        f1 = m // g
        f2 = n // g

        if (f1 * div == str1):
            if (f2 * div == str2):
                return div

        return ""
    

class simpler:
    # Runtime -> 0ms - 100.00%
    # Memory -> 17.83 MB - 46.44%

    # gets rid of all the fluff bs i added
    # basic check, gcd, then just return the value
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 != str2 + str1):
            return ""
        
        g = gcd(len(str1), len(str2))
        return str1[:g]

class betterMemory:
    # Runtime -> 0ms - 100.00%
    # Memory -> 17.78 MB - 71.17%

    # save memory, but saves a bit of memory without the g var
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]