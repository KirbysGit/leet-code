# https://leetcode.com/problems/two-sum/
# easy

class firstAttempt:

    # 01 / 21 / 2026 - 1:01 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 20.76 MB - 5.74%

    # alright i started this one at like 1 am, and i was just sitting looking at
    # it for a while, like how tf is this a hashing problem?

    # my first thought was sorting, but then i realized order mattered, so that
    # ruled out set's and stuff too. and then two ptr method probably would
    # work at some point but it would be O(n^2) as you gotta iterate through
    # every combo of every element.

    # i sat and looked it long enough and in the middle i was like ok if i can 
    # check if its already "in" the hashmap then i can just return the indices.

    # so thats what i did!

    # i also used a defaultdict because i am still not great with dicts
    # and i forget how to do the like setting the value.

    # yea i'm silly, okay so i guess i don't need the defaultdict,
    # because i already do the membership check in the if statement.

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        idk = defaultdict(int)

        for idx in range(len(nums)):

            if nums[idx] in idk:
                return [idk[nums[idx]], idx]
            else:
                idk[target - nums[idx]] = idx