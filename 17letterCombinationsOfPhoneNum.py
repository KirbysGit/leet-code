# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# medium

class firstAttempt:

    # 10 / 27 / 2025 - 1:57 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.68 MB - 92.20%

    # backtracking is weird as hell for me, so i needed some nudges in the right direction
    # but i was just given hints and was able to get the gist other than my classic syntax
    # errors. 

    # first off i was stuck on how we set up the phoneNum dict, like i was like do
    # we need to do the math every time like idx - 1 * 3 but then i was like when
    # we get to 7 or 9 it will be weird. but then a dict made way more sense.

    # then trying to understand the recurse function to properly add the letters
    # while preserving the previous path was weird in my head, i still had graph
    # brain so i was trying to understand how to use a visited array. but the 
    # approach is much easier than that. 
    
    # i understood recursion was needed but main issue was preserving then
    # returning but looking at it now, super simple.

    # first off, because we use class variables, need to reset results. but the major
    # chunk of this problem comes from the recursion. 

    # our base case is checking when idx == n, which means that we have surpassed the 
    # len of our digits and we can add the current path to our results. else,
    # we iterate through the letters for the current digit based on our phoneNum dict,
    # append the current letter to our path, then recurse again with this new path,
    # and an incremented idx, then after recursing all the way through, we come back,
    # pop the current letter, and the continue with the next letter. 



    phoneNum = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}
    results = []

    def recurse(self, idx, path, n, digits):
        if idx == n:
            self.results.append("".join(path))
            return
        
        for ltr in self.phoneNum.get(digits[idx], ""):
            path.append(ltr)
            self.recurse(idx + 1, path, n, digits)
            path.pop()

    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.results = []
        self.recurse(0, [], len(digits), digits)

        return self.results

class otherSolution:

    # simpler looking solution, uses the function inside of the function instead
    # so you don't need any class variables. also doesn't even pass the path, just
    # lets it build and shrink as it goes.

    def letterCombinations(self, digits: str) -> List[str]:

        phone_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9', 'wxyz'}
        result = []
        path = []

        def backtrack(idx):
            if idx = len(digits):
                result.append(''.join(path))
                return

            for ltr in phone_dict[digits[idx]]:
                path.append(ltr)
                backtrack(idx + 1)
                path.pop()

        backtrack(0)
        return result

