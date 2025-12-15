    # https://leetcode.com/problems/reverse-words-in-a-string/
    # medium

    class firstAttempt:
        # 09 / 07 / 2025 - 11:34 pm

        # Runtime -> 4ms - 17.33%
        # Memory -> 17.86 MB - 68.88%

        # idea is to strip the string from its outer characters, then starting from
        # the front, move forward, if the char is not a space, add it to tmp list
        # if char is a space, and tmp is not empty, add tmp to words list, and
        # clear tmp, also while there is a space after current char, move forward
        # at the end, if tmp is not empty, add it to words list, and reverse words list

        # pretty slow but it was the way my C / Java brain was trying to accomplish with
        # python, but i believe python has better ways to do this 
        def reverseWords(self, s: str) -> str:
            s = s.strip()
            asList = list(s)

            front, back = 0, len(asList)
            
            tmp = []
            words = []

            while front < back:
                ch = asList[front]

                if ch != ' ':
                    tmp.append(ch)
                else:
                    if tmp:
                        words.append(''.join(tmp))
                        tmp = []

                    while front + 1 < back and asList[front + 1] == ' ':
                        front+=1

                front += 1

            if tmp:
                words.append(''.join(tmp))

            words.reverse()

            return ' '.join(words)


        class fastAndSimple:

            # Runtime -> 0ms - 100.00%
            # Memory -> 17.73 MB - 91.64% # this is bs, keeps changing

            # didn't know about .split(), but basically does this entire problem for us.    
            # then we just reverse it, and join it back with spaces

            # can be simplified to one line -> return " ".join(s.split()[::-1])

            def reverseWords(self, s: str) -> str:
                s = s.strip()

                return " ".join(s[::-1])

        class with150interview:

            # Runtime -> 0 ms - 100.00%
            # Memory -> 18.04 MB - 23.25%

            def reverseWords(self, s: str) -> str:

                s = s.split()

                front = 0
                back = len(s) - 1

                while front < back:
                    tmp = s[front]
                    s[front] = s[back]
                    s[back] = tmp

                    front +=1 
                    back -= 1

                output = " ".join(s)

                return output

        