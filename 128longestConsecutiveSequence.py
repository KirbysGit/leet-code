# https://leetcode.com/problems/longest-consecutive-sequence/
# medium

class firstAttempt:

    # 01 / 24 / 2026 - 3:24 pm

    # kind of struggling with the implementation, like understanding how to 
    # break it down. but the approach with the hash table as it says in the
    # topics is messing me up.

    # topics are ["Array", "Hash Table", "Union Find"]

    # i just don't really understand how to use the hash table to my
    # advantage if they're not already sorted. 

    # i don't really understand how to do it in O(n), so i'm going to come
    # back to it later. right now i just want to see if i can get some
    # approach going before i learn how to do it.
    
    def longestConsecutive(self, nums: List[int]) -> int:

        check = defaultdict(set)
        
        for idx in range(0, len(nums)):
            if check[nums[idx] - 1]:
                check[nums[idx]] = check[nums[idx] - 1]
                check[nums[idx]].add(nums[idx])
                while check[nums[idx] + 1]:
                    print("In here!", check[nums[idx]])
                    check[nums[idx] + 1] = check[nums[idx] + 1].union(check[nums[idx]])
            else:
                check[nums[idx]].add(nums[idx])

        print(check)