# https://leetcode.com/problems/reverse-vowels-of-a-string/
# easy

class firstAttempt:

    # 09 / 0 / 2025 - 2:15 pm

    # Runtime -> 13 ms - 42.64%
    # Memory -> 20.16 MB - 7.27%

    # idea for me at first was like trying to take out all the vowels,
    # then just reverse them and shove them back in, so doing that, i did a check like
    # go through list, grab vowel by comparing with list of vowels, then save the idx,
    # and the vowel. then reverse the vowels, and shove them back in the idx that you 
    # took them out of

    # pretty slow, i feel like i don't need to save both idx and vowel but in my head
    # im struggling to find a way to do it withotu saving both

    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        toFlip = []
        original = []

        for idx in range(len(s)):
            if s[idx].lower() in vowels:
                original.append(idx)
                toFlip.append(s[idx])

        toFlip = toFlip[::-1]

        toFlip = list(toFlip)
        s = list(s)

        for idx in range(len(original)):
            s[original[idx]] = toFlip[idx]
        
        return ''.join(s)

class moveInAndFlip:
    
    # Runtime -> 15 ms - 39.07%
    # Memory -> 18.66 MB - 48.24%
    
    # saw this idea in one of the faster ones and attempted it myself
    # idea is to have two pointers, one at front and one at the back
    # an outer while loop to continue until front > back, with two 
    # while loops inside to iterate until they each find a vowel, then flip them
    # and then iterate to the next index, and at the end join to make a string

    # time is slower? but im pretty sure its faster


    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        front, back = 0, len(s) - 1
        sList = list(s)
        while (front < back):
            while front < back and sList[front] not in vowels:
                front+=1
            while front < back and sList[back] not in vowels:
                back-=1

            sList[front], sList[back] = sList[back], sList[front]

            front+=1
            back-=1

        s = ''.join(sList)

        return s

class vowelsAsSet:

    # Runtime -> 3 ms - 99.65%
    # Memory -> 18.66 MB - 48.24%

    # alright similar to the two pointer in the last one, however i wasn't 
    # thinking about how we are parsing through the vowels string each time
    # so by using a set and just referencing it like that, we can save a bunch of time

    # memory didn't really change though

    VOWELS = set('aeiouAEIOU')

    def reverseVowels(self, s: str) -> str:
        
        s_list = list(s)
        i, j = 0, len(s_list) - 1

        while i < j:
            while i < j and s_list[i] not in VOWELS:
                i += 1
            while i < j and s_list[j] not in VOWELS:
                j -= 1
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1

        return ''.join(s_list)