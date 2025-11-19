# https://leetcode.com/problems/remove-element/
# easy

class firstAttempt:

    # 11 / 19 / 2025 - 12:30 am

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.76 MB - 52.72%

    # had to get one hint becasue i knew my solution was working but it wasn't
    # saying it was correct. 

    # i was counting the number of elements that were the value, which causes the
    # output to be incorrect.

    # but anyways, idea was how can we remove the elements we don't want? pop em!

    # so if it was the element, pop the idx, then decrement the length of list, then continue
    # else, increment index and count.

    # at the end return the count as the list adjustments were made in place.

    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        count = 0
        n = len(nums)

        while i < n:
            if (nums[i] == val):
                nums.pop(i)
                n-=1
                continue

            count+=1
            i += 1

        return count

class simpleSolution:

    # just saw it, same speed but looks cleaner.

    # same sort of thing, but just an extra pointer to keep track of the index of the last
    # non-val element.

    k = 0
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

