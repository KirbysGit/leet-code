# https://leetcode.com/problems/decode-string/
# medium

class firstAttempt:
    
    # alright i had to use chatgpt completely, i have to realy take time to understand
    # this one.

    # 09 / 23 / 2025 - 3:45 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.68 MB - 84.29%

    # so first off we set up,
    #   pairStack - stack to remember old state
    #   cur - current decoded string we're building
    #   k - number of repeats for next bracketed block

    # then we iterate through decoded string,
    #   if char is a digit, we update k to be k * 10 + int(char)
    #   if char is a [ , we push cur and k to pairStack then reset em
    #   if char is a ] , we pop from pairStack, then update cur to be ltr + cur * num
    #   else we just add the char to cur

    # then we return it

    # the issues for me isn't as much in the code but understanding how i 
    # am supposed to connect those dots in my head, like i was really getting caught on
    # brackets within brackets, like i knew a stack would work, but how would we store
    # and handle bracketed strings. still got some work to do with this one.

    def decodeString(self, s: str) -> str:
        
        pairStack = []
        cur = ""
        k=0
        decode = list(s)

        for char in decode:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                pairStack.append((cur, k))
                cur = ""
                k = 0
            elif char == ']':
                ltr, num = pairStack.pop()
                cur = ltr + cur * num
            else:
                cur += char

        return cur