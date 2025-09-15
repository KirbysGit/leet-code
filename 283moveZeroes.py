# https://leetcode.com/problems/move-zeroes/
# easy

class firstAttempt:
    # 09 / 11 / 2025 - 3:04 pm

    # Runtime -> 19ms - 13.77%
    # Memory -> 18.74 MB - 79.60%

    # first idea was two pointers, but i realized swapping the indexes was pretty stupid
    # because you have to handle so many more edge cases

    # so i came up with this, idea is just to iterate through a set number of indices
    # if the current index is a 0, delete it and add a 0 to the end, but i realized
    # i kept getting issues because the index was changing so i used a counter that i
    # named time for literally no reason

    # it works but its pretty slow
    def moveZeroes(self, nums: List[int]) -> None:
        
        idx = 0
        time = 0

        while time < len(nums) - 1:
            if nums[idx] == 0:
                del nums[idx]
                nums += [0]
            else:
                idx+=1

            time+=1

        
        return nums

class optimizedSpeed:

    # Runtime -> 0ms - 100.00%
    # Memory -> 19.10 - 9.87%

    # had to get some hints from mr.gpt for this, apparently del is really slow,
    # and i didn't know that, so this method basically was my original idea that i 
    # couldn't get to work, but basically go through the list, if zero, 
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 

        for j in range(0, len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i+=1

        while i < len(nums):
            nums[i] = 0
            i+=1


class optimizedMemory:

    # alright i think leetcode is jsut dumb, because the only difference is a while
    # versus a for loop, but somehow this has better memory?

    # no idea
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for j in range(k,len(nums)):
            nums[j]=0