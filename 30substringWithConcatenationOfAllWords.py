# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# hard

class firstAttempt:

    # 01 / 04 / 2026 - 2:42 pm

    # still not done. stupid ah problem.

    # i think im on the right track but i can tell my solution is boutta be slow as hell.

    # basically i am running into an issue with our first test case where i get the [0] index
    # properly but the [0, 9] i can't get. pretty sure its because the way i designate  front is based
    # on the larger string, but i reference the front inside of the sub string here.

    # sub = string[front:(front + wordL)]

    # so i need to go back through and break down how i should use the variables for this. 

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        start = 0
        wordL = len(words[0])
        window = wordL * len(words)
        back = start + window
        n = len(words)

        seen = []
        final = []

        while back < len(s):
            front = start
            back = front + window
            string = s[front:back]
            
            print(string)
            while front < back:
                sub = string[front:(front+wordL)]
                if string == "foobar":
                    print(seen)
                if sub in words and sub not in seen:
                    seen.append(sub)
                    front += wordL
                else:
                    break

            if len(seen) == n:
                final.append(start)
            
            start += wordL
            seen = []     

        return final

        # coming back fix that error then we'll probably run into something else.