# https://leetcode.com/problems/edit-distance/
# medium

class firstAttempt:

    # 11 / 05 / 2025 - 1:57 pm

    # Runtime -> 60 ms - 65.39%
    # Memory -> 21.17 MB - 56.12%

    # alright basically this follows a pretty similar pattern, but my brain literally
    # still cannot wrap my head around how it breaks down the problem to its own
    # like subproblems that we can then focus then increment off of.
    
    # like for this problem, when i was first staring at it wondering how to best
    # break it down, i had no understanding of how to both preserve order and also
    # find the quickest way to get from one word to the other, like knowing that
    # if we replace THEN delete one it would be faster (that was just a general example)

    # then after some advice from mrGPT, it broke it down in terms of the grid which
    # i was already trying to break down previously, like i get how it references
    # but its hard to connect that if we move horizontally on the grid, it is like
    # we are deleting a character, if we move vertically its like we are adding
    # a character, and moving diagonally is where we replace a character. 

    # so once we had those three states it was more of a matter of figuring out the grid
    # because we have to handle the extra boundaries of the grid but also verify that
    # we get the minimum distance out of our three options, assuming the characters are
    # not just the same. thats how we landed upon this set up.

    # my biggest struggles was 1. general understanding of the problem (WOOHOO!!!!), and
    # 2. setting up the indexing for the grid.

    # but here is the solution, basically what i broke down above but i'll do it again
    # because who cares.

    # 1. initialize grid with extra boundaries to handle backwards indexing.
    # 2. set first row and column to index of current char.
    # 3. iterate through grid, checking if chars are the same.
    # 4. if chars are same, grab diagonal value and set it.
    # 5. if chars are diff, grab value from left, top, and diagonal, then add 1 to the min.
    # 6. then return!

    # dp is still so weird to connect in my head, i gotta take some notes on it.

    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
                    
        return dp[i][j]
