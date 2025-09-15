# https://leetcode.com/problems/is-subsequence/
# easy

class firstAttempt:

    # 09 / 11 / 2025 - 4:04 pm

    # Runtime -> 0ms - 100.00%
    # Memory -> 17.79 MB - 68.06%

    # this one was all on my own, except i got a hint from chatGPT on removing chars from list
    # but my idea was the same since the start

    # i tried the double pointer, but it was just not working with the old approach of just
    # checking the length, but instead doing this with the new string made it was easier
    
    # i was trying to avoid that tho because i didn't want the extra memory, but this is a 
    # good start. 

    # so whats going on is, initial check for empty string, (def a better way to do this)
    # then iterate through t, if len(s) == len(new_t) return True to handle the case where
    # i is incremented past the end of s
    # then check if the current char in t is same as current char in s, then if so
    # add it to new_t and increment idx (s's pointer)
    # then a final check for if the strings are the same
    # else return False

    # definitely some things i see that don't seem optimal like the final check seems
    # unnecessary, as well as the inital check, there is def a way to do both in like one line

    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0

        if(s == ""):
            return True

        new_t = ""

        for char in t:
            if (len(s) == len(new_t)):
                return True
                
            if s[idx] == char:
                new_t += char
                idx+=1
        
        if(s == new_t):
            return True

        return False

class originalIdeaWorking:

    # this is what i was trying to create earlier on, but i def messed up how i was
    # incrementing them, see how you don't need the initial check for empty string,
    # or the multiple return True statements. much simpler, but not that much faster,
    # because the logic is the same, but just not as clean

    # Runtime -> 0ms - 100.00%
    # Memory -> 17.90 MB - 24.47%

    def isSubsequence(self, s: str, t: str) -> bool:
        left=right=0

        while left<len(s) and right<len(t):
            if s[left]==t[right]:
                left+=1
                right+=1
            else:
                right+=1
        if left==len(s):
            return True
        else:
            return False