# https://leetcode.com/problems/majority-element/
# easy

class firstAttempt:
    
    # 11 / 22 / 2025 - 2:21 pm
    
    # Runtime -> 9 ms - 33.79%
    # Memory -> 19.41 MB - 19.25%

    # had to use chatgpt because im not great with dictionaries, but
    # i tried one approach with like a just counter, because i thought it was out
    # of only two elements but that was wrong. so i was like its gonna be o(n)
    # either way so i just use like a hashmap to count frequency, then take
    # the max value based on the count.

    def majorityElement(self, nums: List[int]) -> int:
        
        my = {}

        for num in nums:
            my[num] = my.get(num, 0) + 1
        
        return max(my, key=my.get)

class holyGenius:

    # 11 / 22 / 2025 - 2:23 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.31 MB - 51.15%

    # this is crazy smart. basically, use sort the arry, and return the middle element
    # as if its majority it will be at the middle. 

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]