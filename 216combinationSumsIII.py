# https://leetcode.com/problems/combination-sum-iii/
# medium

class firstAttempt:

    # 10 / 28 / 2025 - 2:02 

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.94 MB - 16.49%

    # i used chatgpt for 3 chars for this one. 3 CHARS!!!

    # nah i mean i did reference my notebook from yesterdays problem which is basically
    # an identical set up, except handling the condition is different. but my issue
    # was i kept .append(path) which would just add the same path to the results
    # over and over again. we needed to make a copy then append it to the results.

    # so basically doing result.append(path[:]) instead of just result.append(path)

    # so basically i set it up as an idx sort of thing, definitely could be done
    # without idx but i felt it was easier to handle the range values for the loop.

    # but initialize nums array, then in the meat of our solution, the recurse function
    # the base case comes back to checking the len of the current path, and if it is
    # equal to k, then we check the sum of this path, if its equal to n, then we append
    # it to our results array then return.

    # if the len of the path is not equal to k then we iterate through the nums array,
    # except using a smaller range since we can't have duplicates, then we add the 
    # current num to our path, recurse again, then after coming back, pop the current 
    # value and move on.

    # we call the recurse on idx x and then return the results of that.

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        path = []

        def recurse(idx):
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return
                
            for i in range(idx, len(nums)):
                path.append(nums[i])
                recurse(i + 1)
                path.pop()
            
        recurse(0)

        return result