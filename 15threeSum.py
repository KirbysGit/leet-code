# https://leetcode.com/problems/3sum/
# medium

class firstAttempt:

    # 12 / 24 / 2025 - 1:50 am

    # its christmas eve and im going home and idk when i would be able to do this other than
    # before work but i don't want to stress myself out over not getting it done and breaking
    # my github streak, so im adding this from the night before. 

    # first attempt, like i looked through and was like "this should work". update: it does NOT!

    # but i definitely think i can figure it out, just gonna come back to it tmrw.

    class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        n = len(nums)
        front = 1
        walk = front + 1
        final = []

        while front < n - 1:
            pair = nums[front - 1] + nums[front]
            while walk < n:
                if pair + nums[walk] == 0:
                    final.append([nums[front], nums[front - 1], nums[walk]])

                walk += 1

            front += 1
            walk = front + 1
        
        return final

class secondAttempt:

    # its christmas!!! i work in like less than an hour so i can't really attempt the code,
    # but i'm thinking like a greedy approach to it so we can sort the array and then iterate
    # through the array using three numbers that add to 0 because order doesn't matter.

    # and we're back again!

    # 12 / 26 / 2025 - 2:46 pm

    # this one is hurting my brain, its a better approach, but when we use a set it causes like
    # a overlap of when we check the "if in". im struggling to find a way.

    # i wrote out on my whiteboard this approach :

    # "once its sorted we know we can directly look for a value, like just do the pair then,
    # if the value is in the set then add the pair + value to a [] and check if thats already
    # in final output and if not, add it, if so skip."

    # and i tried to implement but i ran into an issue with this test case : 

    # [-100,-70,-60,110,120,130,160]

    # and i feel stupid as hell, because what my approach is, its like a window of checking,
    # what we need it to do is like check each different trio, but i don't get how we can
    # do it without O(n^2), and thats what im trying to avoid.

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        check = set(nums)

        if n == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        
        pair = 1
        look = pair + 1
        output = []

        while pair < n - 1:
            needed = 0 - (nums[pair] + nums[pair - 1])
            if needed in check:
                toAdd = sorted([nums[pair - 1], nums[pair], needed])
                if toAdd not in output:
                    output.append(toAdd)

            pair += 1
        
        return output

class thirdAttempt:

    # holy shit this is taking me so long. i'm just kind of stuck now, 
    # i was trying to think of an approach with our sorted method but it really just does not work.

    # 12 / 27 / 2025 - 2:40 pm

    # im at 310 / 315 test cases, i think my approach is borderline O(n^2). i'm trying
    # to think of a break case to stop the pointer movements before they go too far but im struggling to find it

    # this is my current code, basically same approach as before except i lock one value and just move
    # through the rest.
    
    # alright im leaving off, but this problem is so silly!! 

    # i'm a point where im trying to break down some of my set up to see whats taking so long
    # like i tried the initial sort removal but that messed up a lot of the test cases, and then
    # also i know for a fact that we run into a lot of the same solutions and i have to check
    # "if ... in" which takes a long time, so im trying to figure out what i can remove to take
    # a step towards a more greedy approach. 

    # i refuse to use gpt on this right now. i got it, it will come to me fs soon.

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        if n == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        nums.sort()
        output = []
        front = 0
        back = n - 1

        for idx, val in enumerate(nums):
            while front < back:
                if front == idx:
                    front += 1
                    continue
                elif back == idx:
                    back -= 1
                    continue
                    
                if nums[front] + nums[back] == (0 - val):
                    toAdd = sorted([nums[front], nums[back], val])
                    if toAdd not in output:
                        output.append(toAdd)
                    front += 1
                elif nums[front] + nums[back] < (0 - val):
                    front += 1
                else:
                    back -= 1

            front = 0
            back = n - 1 

        return output

class fourthAttempt:

    # alright i feel stupid as fuck stilL!!!!

    # 12 / 28 / 2025

    # just put like an hour and a half into this. just trying to understand how i can do this without O(n^2)

    # i used the hints and still don't understand, one of them mentioned a hash map which i kind of want to try.

    # but im really bad with dictionaries so....

    # might try again later tn because its pissing me off.

    # probably at like 8 hours spent on this problem.

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        if n == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        nums.sort()
        output = []
        front = 0
        back = n - 1

        for idx, val in enumerate(nums):
            while front < back:
                if front == idx:
                    front += 1
                    continue
                elif back == idx:
                    back -= 1
                    continue
                
                if nums[front] > 0 and nums[back] > 0 and val > 0:
                    break
                
                if nums[front] < 0 and nums[back] < 0 and val < 0:
                    break

                if nums[front] + nums[back] + val == 0:
                    toAdd = sorted([nums[front], nums[back], val])
                    if toAdd not in output:
                        output.append(toAdd)
                    front += 1
                elif nums[front] + nums[back] + val < 0:
                    front += 1
                else:
                    back -= 1

            front = 0
            back = n - 1 

        return output