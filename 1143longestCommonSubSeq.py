# https://leetcode.com/problems/longest-common-subsequence/
# medium

class firstAttempt:

    # 11 / 03 / 2025 - 6:06 pm

    # Runtime -> 380 ms - 93.34%
    # Memory -> 25.41 MB - 88.41%

    # okay so i spent a lot of time on this one, i got all the way through where i was like
    # okay i got it set up perfectly, but i just don't get how dp is necessary. but that was
    # when i realized the cases can have it where the longest subsequence isn't just the
    # the first subsequence, its the longest available. 

    # so that messed me up a bit and i had to use mrgpt to help me break down my thoughts, 
    # because leetcode gave me the hints on how to set up the dp array. like the double array,
    # but i didn't understand the overall set up of the indexing. 

    # alright after a bit of breakdown i think i got it. outside of the normal set up with
    # the initialize loop, then iterate through the text1 and text2. we do the + 1 to handle
    # the boundaries better, because think about some of the past arrays we have set up
    # like for the robot maze one, think about how we initialize all the edges to 1, we're
    # doing the same sort of thing here, just extending the array a bit to have like a "wall"
    # of zeros to reference as we grow diagonally.

    # but anyways, the magic from this comes from our check of the current characters
    # that are being looked at. if they are the same, we add the 1 to the value of the
    # cells that are one to the left and one up from the current cell, this helps
    # us track the best subsequence, because say in a case where we have a letter 
    # that is the same earlier on, we don't just try to build off that letter, (this was
    # my issue earlier) but instead we start fresh with the new letter to see if
    # there is a better subsequence out there for the current characters.

    # so basically if they are the same, check diagonal up, then add 1 to that.
    # if not, check cell to left and up, then take max of those two.

    # then return the final cell in the array, as it will have preserved the best
    # subsequence.

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if (text1 == text2):
            return len(text1)

        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):    
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[i][j]