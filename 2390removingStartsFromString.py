# https://leetcode.com/problems/removing-stars-from-a-string/
# medium

class firstAttempt:

    # alright i had to use chatgpt to ask how to set it up for why it was too slow

    # here is what i did first, but it hit time limit exceeded

    # because i was popping the indexes from the middle

    def removeStars(self, s: str) -> str:
        
        idx = 0

        starList = list(s)

        while (idx < len(starList)):
            if (starList[idx] == '*'):
                starList.pop(idx)
                idx-=1
                starList.pop(idx)
            else:
                idx+=1

        return "".join(starList)

class firstAccepted:

    # 09 / 22 / 2025 - 1:46 pm

    # Runtime -> 160 ms - 16.69%
    # Memory -> 19.00 MB - 79.18%

    # idea is to use a stack which i understood, but i wasn't sure how to set it up
    # but with this we create a new string, adding chars to it, and if we see a star,
    # pop the last char we added, if not a star, we add the char to the string

    # pretty simple, but pretty slow

    def removeStars(self, s: str) -> str:

        short = []

        for char in s:
            if char == '*':
                short.pop()
            else:
                short += char

        return "".join(short)


class appendNotIncrement:

    # Runtime -> 84 ms - 95.32%
    # Memory -> 19.25 MB - 24.40%

    # literally changed one line, from the " += char " to the " append(char) "

    # apparently += has to iterate the string, so its way slower if we get up to longer strings
    
    def removeStars(self, s: str) -> str:

        short = []

        for char in s:
            if char == '*':
                short.pop()
            else:
                short.append(char)

        return "".join(short)