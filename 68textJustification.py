# https://leetcode.com/problems/text-justification/
# hard

class firstAttempt:

    # 12 / 19 / 2025 - 3:13 pm 

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.27 MB - 99.97%

    # alright so i had to use chatgpt for the justification, but i think i was just 
    # lazy because i know i would've been able to do it. my written out logic was spot on!

    # but anyways im just going to copy and paste the code because theres a lot to it.

    # i used addSpaces as like the center justify function.
    # i used leftJustify as like the left justify function just for the last row.
    
    # then the main logic is just iterating through the words, and adding them to the line,
    # and then if the line is too long, we justify it, and then add it to the output.

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def addSpaces(string, numSpaces, maxWidth) -> str:
            chars = list(string)

            if " " not in chars:
                chars.append(" " * numSpaces)
                return "".join(chars)

            while numSpaces > 0:
                idx = 0

                while idx < len(chars) - 1:
                    if chars[idx] == " " and chars[idx + 1] != " ":
                        chars.insert(idx + 1, " ")
                        numSpaces -= 1
                        idx += 2
                    else:
                        idx += 1
                    
                    if numSpaces == 0:
                        break

            return "".join(chars)

        def leftJustify(string, numSpaces) -> str:
            spaces = " " * numSpaces
            myList = list(string)
            myList.append(spaces)
            return "".join(myList)


        line = ""
        output = []
        i = 0

        while i < len(words):
            l = len(line)
            word = words[i]
            w = len(word) if l == 0 else len(word) + 1

            if w + l <= maxWidth:
                if w > len(word):
                    line += " "
                line += word
                i += 1
                continue
            else:
                spaces = maxWidth - l
                line = addSpaces(line, spaces, maxWidth)
                output.append(line)
                line = ""

        l = len(line)
        if l != 0:
            spaces = maxWidth - l
            line = leftJustify(line, spaces)
            output.append(line)
    
        return output

            
