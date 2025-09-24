# https://leetcode.com/problems/unique-number-of-occurrences/
# easy

class firstAttempt:

    # 09 / 19 / 2025 - 3:03 pm

    # Runtime -> 0ms - 100.00%
    # Memory -> 17.94 MB - 40.04%

    # had to use chatgpt just because i don't understand the tools, i had the right idea,
    # but i just couldn't understand how to get around it just using an array, so i
    # asked how to use a dictionary and that was basically all it took for the answer.

    # but the idea is really simple, set up an dictionary (hashmap), then loop through
    # every number in arr, 

    # then we increment count[num] which basically just looks up the key 'num' in the 
    # dict and stores / updates its value. then the .get(num, 0) is basically, get the current
    # value at num if it exists, otherwise give me 0. then we add 1 to it.

    # then we convert the values of the dictionary back into a list, and then we use
    # set's unique ability to check if the list has any duplicates, if it does, then 
    # the length will be different, if they're the same length, return true, else, false.
    
    # simply put:
    #  - count frequency
    #  - check if frequency is unique using set

    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        counts = list(count.values())

        return len(counts) == len(set(counts))