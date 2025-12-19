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
    
    # this is what i wrote out on my whiteboard :

    # iterate through words ::
    #   checking cur length of line.
    #   if adding cur word to list w/ a space will be over maxWidth.
    #       justify row with spaces.
    #           # do this by working from L -> R, and per space char
    #           # we run into, check if next char is a space too,
    #               # if so, continue.
    #               # else, insert a space and decrement numSpaces.
    #           # do this until numSpaces is 0.
    #       then add line to output and reset line to empty.
    #   else.
    #       add word with space and continue.

    # some of the extra lings i had to do was handle like a single word case that doesn't fit
    # entire line, which i handled by checking if " " is not in chars, then we add the spaces 
    # to end of the line in our addSpaces.

    # also added the leftJustify function to handle that last row case, which now in hindsight
    # im doing the exact same thing in the addSpaces, but it kind of needed to be separate 
    # because it would justify the space if there was any in the last row, but the goal is 
    # just to add the spaces to the end of the row.

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

            
