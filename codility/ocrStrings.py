# from same interview OA as spike.py.

# basically, we are given two strings. they have like OCR applied to them or something.

# the word AppLe, could be OCR'd as 2pL1 or A2Le, and they could be the same word.

# or for somethign like abbbbbbbbba could be OCR'd as a10 or 10a. 

# our job in this question is to determine if the two strings, S & T, could be the same word.

# input -> "3x2x" and "8"
# output -> False
# reasoning -> the len of the first string can only go up to 7.

# input -> "10a" and "a10"
# output -> True
# reasoning -> they can be the same.

# input -> "ba1" and "1Ad"
# output -> False
# reasoning -> the 'a' vs 'A' difference matters so that they aren't the same.

class myAttempt:

    # 01 / 21 / 2026 - 7:44 pm

    # S & T are the two strings.

    # this problem is still super weird in my brain so im going to do a walk through to understand it better with the AppLe example.

    # input -> "A2Le" and "2pL1"

    # initial state :
    # i = 0, j = 0
    # skipS = 0, skipT = 0

    # iteration 1 :
    # S[0] = 'A' -> not a digit
    # T[0] = '2' -> is a digit
    # skipT = 2
    # j = 1
    # continue
    # (no original character consumed yet)

    # iteration 2 :
    # S[0] = 'A' -> not a digit
    # T[1] = 'p' -> not a digit
    # skipT > 0, skipS == 0
    # consume one original character
    # S supplies letter 'A'  -> i = 1
    # T consumes skip        -> skipT = 1
    # continue

    # iteration 3 :
    # S[1] = '2' -> is a digit
    # skipS = 2
    # i = 2
    # continue
    # (no original character consumed yet)

    # iteration 4 :
    # S[2] = 'L' -> not a digit
    # T[1] = 'p' -> not a digit
    # skipS > 0 and skipT > 0
    # consume one original character
    # S consumes skip -> skipS = 1
    # T consumes skip -> skipT = 0
    # continue

    # iteration 5 :
    # S[2] = 'L' -> not a digit
    # T[1] = 'p' -> not a digit
    # skipS > 0, skipT == 0
    # consume one original character
    # S consumes skip -> skipS = 0
    # T supplies letter 'p' -> j = 2
    # continue

    # iteration 6 :
    # S[2] = 'L' -> not a digit
    # T[2] = 'L' -> not a digit
    # skipS == 0 and skipT == 0
    # both must give letters
    # compare 'L' == 'L' ✔
    # consume one original character
    # i = 3
    # j = 3
    # continue

    # iteration 7 :
    # S[3] = 'e' -> not a digit
    # T[3] = '1' -> is a digit
    # skipT = 1
    # j = 4
    # continue
    # (no original character consumed yet)

    # iteration 8 :
    # S[3] = 'e' -> not a digit
    # j == len(T)
    # skipT > 0, skipS == 0
    # consume one original character
    # S supplies letter 'e' -> i = 4
    # T consumes skip       -> skipT = 0
    # continue

    # loop ends :
    # i == len(S)
    # j == len(T)
    # skipS == 0
    # skipT == 0
    # return True

    def ocrStrings(S, T):

        i = j = 0
        skipS = skipT = 0

        while i < len(S) and j < len(T):

            if i < len(S) and S[i].isdigit():
                skipS = skipS * 10 + int(S[i])
                i += 1
                continue

            if j < len(T) and T[j].isdigit():
                skipT = skipT * 10 + int(T[j])
                j += 1
                continue

            if skipS > 0 or skipT > 0:
                if skipS > 0:
                    skipS -= 1
                else:
                    if i >= len(S):
                        return False
                    i += 1

                if skipT > 0:
                    skipT -= 1
                else:
                    if j >= len(T):
                        return False
                    j += 1

                continue

            if i >= len(S) or j >= len(T):
                return False

            if S[i] != T[j]:
                return False

            i += 1
            j += 1

        return skipS == 0 and skipT == 0
