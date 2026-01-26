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

class workingAttempt:

    # 01 / 25 / 2026 - 8:23 pm

    # Runtime -> 47 ms - 69.53%
    # Memory -> 36.68 MB - 32.53%

    # had to use chatgpt for this, i was really trying to understand how to use the sets, like i was
    # using a dictionary of sets, but it wasn't really working out because i would get these partial
    # sets. 

    # i used chatgpt for some hints, it didn't give me the direct answer but it mentioned just using
    # a set as a seen array and i was like ohhh im stupid asf!! like just using a set to add values
    # then referencing the set to see if any sequences are possible from the values.

    # but in my mind it still is pretty weird that its not O(n^2) as we use a while loop, but i guess
    # thats just the power of sets and how they work.

    # so this approach below with the help of chatgpt really just creates a seen set, then goes back
    # through checking if we've seen the value - 1, we skip because that means we will count it
    # at some other point so this helps us avoid counting through partial sequences twice.

    # if we haven't seen it then we iterate through the values that exist checking if they are
    # in the set, and increment our sequence length pointer and update the max if its greater.

    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        out = set()

        for num in nums:
            out.add(num)

        best = 0

        for num in nums:
            if num - 1 not in out:
                val = num
                seq = 1
                while val + 1 in out:
                    val += 1
                    seq += 1
                
                best = max(best, seq)

        return best