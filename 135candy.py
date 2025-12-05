# https://leetcode.com/problems/candy/
# hard - FIRST HARD PROBLEM ALL BY MYSELF!!!

class firstAttempt:

    # 12 / 05 / 2025 - 1:03 pm
    
    # Runtime -> 14 ms - 75.34%
    # Memory -> 19.96 MB - 34.99%

    # all by myself. yuhp im goated.

    # it took me a minute, i tried multiple different approaches walking through in my brain
    # first one was just like incrementing a total value, but then i was like damn we kinda
    # gotta keep track of what the value before or after it is. so i was like we actually need
    # that extra array to keep track of the candy values per kid. 

    # once i realized that, i was like okay we need to keep track of the values per kid, but how
    # can we do that from forwards and backwards? i was thinking about a sliding window approach but
    # that doesn't really aggregate correclty moving both directions. so i was like okay we need
    # to figure out how to track that, and they i remembered the two pass from a couple questions ago.

    # i implemented that, but ran into a bunc hof issues with just incrementing the candies by one,
    # because we needed to add them based off the values before and after it, so we needed to reference that
    # and once i had that it was pretty much set to what we did below.

    # one forward pass aggregating the values. and a second pass checking the values backwards just
    # with an extra check to make sure we don't increment if we don't need to.

    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        candy = [1] * n

        for idx in range(1, n):
            if ratings[idx] > ratings[idx - 1]:
                candy[idx] = candy[idx - 1] + 1
        
        for idx in range(n - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1] and candy[idx] <= candy[idx + 1]:
                candy[idx] = candy[idx + 1] + 1
        
        total = sum(candy)

        return total