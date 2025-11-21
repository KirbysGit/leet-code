# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# medium

class firstAttempt:

    # 11 / 21 / 2025 - 2:46 pm 

    # Runtime -> 105 ms - 7.85%
    # Memory -> 20.35 MB - 79.40%

    # alright so i was thinking and tried to use chatgpt for a hint but it didn't really help me out, 
    # so this one kind of sets up a sliding points with a very slow while loop that just removes the
    # duplicates after it finds a pair of values that are duplicates, just increment up one and compare
    # the rest continuously until the end of the array.

    # else, meaning they're not the same, just keep incrementing up through the pointers.
    # then we return the length of the array.

    # i did it myself so i like it but its definitely slow. i think the pop combined with the while loop
    # is very inefficient.

    def removeDuplicates(self, nums: List[int]) -> int:
        
        read = 1
        write = 0

        while read < len(nums):
            if nums[write] == nums[read]:
                write += 1
                read += 1
                while read < len(nums) and write < len(nums) and nums[write] == nums[read]:
                    nums.pop(read)
                continue
            
            write += 1
            read += 1
            
        return len(nums)

class simpleButStillSLower:

    # just tried this :

    # 11 / 21 / 2025 - 2:52 pm

    # Runtime -> 88 ms - 37.67%

    def removeDuplicates(self, nums: List[int]) -> int:
        
        i, j = 0, 2

        while j < len(nums):
            if nums[j] == nums[i]:
                nums.pop(j)
            else:
                i += 1
                j += 1

class justAsSlow:

    # 11 / 21 / 2025 - 2:58 pm

    # Runtime -> 89 ms - 32.96%

    def removeDuplicates(self, nums: List[int]) -> int:
        
        read, write = 2, 2

        while read < len(nums):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
            
            read += 1

        return write
   

class better:

    # 11 / 21 / 2025 - 3:01 pm

    # Runtime -> 82 ms - 70.96%

    # used solutions tab for this one because i didn't understand why the last
    # one was still slow. but this is the best one we got, basically just same
    # sort of thing with a for loop.

    def removeDuplicates(self, nums: List[int]) -> int:

        write = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        
        return write
