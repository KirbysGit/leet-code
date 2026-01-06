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

class secondAttempt:

    # 01 / 05 / 2026 - 3:07 pm

    # still working on it. 

    # i got some test cases working. currently 76 / 182 test cases with my approach.

    # submitted and realized i don't really consider duplicate words which is a big issue because it will just
    # attach the word to the seen array and just kind of forget about it.

    # i consulted chatGPT because i want to make a bit more progress with how i go through these problems,
    # if i just struggled through this it might take me like a week versus like 2 days and some assistance.

    # the approach i got was to use a dictionary to count the frequency of each word in the words list.
    # then we iterate through the string s in windows of size len(words) * len(words[0]), and for each window.
    # but i'm not going to do that right now, when i come back i will.

    # pretty similar approach to yesterday but i just updated it to work.

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        front, end = 0, 0
        subStr = len(words[0])
        window = len(words[0]) * len(words)
        output = []

        while end < len(s):
            seen = []

            start = front
            end = start + window

            while start < end:
                sub = s[start:(start + subStr)]
                if sub in words and sub not in seen:
                    seen.append(sub)
                    start += subStr
                else:
                    break
            
            if len(seen) == len(words):
                output.append(front)
            
            front += subStr

        return output


class thirdAttempt:

    # shits pissing me off.

    # 1 / 05 / 2026 - 8:21 pm

    # trying to do the sliding window with the counter but theres so many small things that 
    # are just hurting my brain. like so many cases i need to consider. 

    # coming back to this tmrw. trying to figure out ordering and counter. 

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        subStrings = {}
        for word in words:
            subStrings[word] = subStrings.setdefault(word, 0) + 1

        wordLength = len(words[0])

        front = 0
        count = 0
        noMore = len(words)

        res = []
        current = {}

        for idx in range(0, len(s), wordLength):

            if count < noMore:
                inp = s[idx:(idx + wordLength)]
                current[inp] = current.setdefault(inp, 0) + 1
                count += 1

            if count == noMore:
                if subStrings == current:
                    res.append(front)

            if count > noMore:
                out = s[front:(front + wordLength)]
                current[out] = current.get(out, 0) - 1
                front += wordLength

            count += 1

        return res