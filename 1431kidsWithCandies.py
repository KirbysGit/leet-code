# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# easy

# almost all the mem optimized solutions are the same as this one
# leetCode is weird though, i ran max mem solution and it gave me same vals

class firstAttempt:

    # 09 / 05 / 2025 - 2:27 pm

    # Runtime -> 0ms - 100.00%
    # Memory -> 17.62 MB - 84.80%

    # set an initial array of all false
    # find highest value in array
    
    # iterate through array, if the cur val + extraCandies is greater than
    # or equal to the highest value, set the cur index to true

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        truthArr = [False] * len(candies)
        maxVal = max(candies)

        for kid in range(len(candies)):
            if candies[kid] + extraCandies >= maxVal:
                truthArr[kid] = True

        return truthArr
