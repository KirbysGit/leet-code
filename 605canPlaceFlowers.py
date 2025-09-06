# https://leetcode.com/problems/can-place-flowers/
# easy

class firstAttempt:

    # 09 / 05 / 2025 - 3:12 pm

    # Runtime -> 12ms - 21.48%
    # Memory -> 18.13 MB - 54.39%

    # took me a couple iterations, but i tried handling the edge cases as its own thing
    # but that didn't work well, ended up with this, pretty inefficient but it works

    # idea is iterate through flowerbed, if cur is 0, check if left and right are empty
    # if so, set the cur value to 1, increment the goal, and then skip the next index

    # i already see ways to optimize this like getting rid of goal and just decrementing 
    # n instead

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        goal = 0
        flower = 0

        while (flower < len(flowerbed)):
            if (flowerbed[flower] == 0):
                left_empty = flower == 0 or flowerbed[flower - 1] == 0
                right_empty = flower == len(flowerbed) - 1 or flowerbed[flower + 1] == 0
                if left_empty and right_empty:
                    flowerbed[flower] = 1
                    goal+=1
                    flower+=2
                    continue
            flower +=1

        if (goal >= n):
            return True


        return False


class removingGoal:

    # Runtime -> 7ms - 72.58%
    # Memory -> 18.19MB - 54.39%

    # idea is to get rid of the goal variable and decrement n instead

    class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flower = 0

        while (flower < len(flowerbed) and n > 0):
            if (flowerbed[flower] == 0):
                left_empty = flower == 0 or flowerbed[flower - 1] == 0
                right_empty = flower == len(flowerbed) - 1 or flowerbed[flower + 1] == 0
                if left_empty and right_empty:
                    flowerbed[flower] = 1
                    n-=1
                    flower+=2
                    continue
            flower +=1

        if (n <= 0):
            return True

        return False


class expandingList:

    # Runtime -> 4ms - 85.75%
    # Memory -> 18.10MB - 82.56%

    # same thing except we add 0 to beginning and end of list
    # then same iteration except no handling of edge cases
    # also added a check for n <= 0 in the loop to save time

    # time is faster because no check for edge cases, but also at the same time
    # leet code depending on when you run it, it will give different results

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if (flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if (n <= 0):
                    return True

        return n<=0