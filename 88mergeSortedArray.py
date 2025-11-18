# https://leetcode.com/problems/merge-sorted-array/
# easy

class firstAttempt:

    # 11 / 18 / 2025 - 3:28 pm

    # Runtime -> 0 ms - 100.00% 
    # Memory -> 18.07 MB - 25.48%

    # alright so for this one, i definitely struggled through it for a bit
    # i just couldn't wrap my head around setting it up for the 0's to get rid of them.

    # chatgpt gave me a hint and said work from the back, so i set it up for that, but then
    # when i got to the point where there was a bit of overlap in terms of the integers, 
    # i was like oh shit it doesn't work, and i couldn't really figure out how to handle it.
    
    # ill put the solution below. 

    # basically, handling the first edge cases, where either m or n is empty, 
    # just return other array basically. then for the main case, we had to use 3 pointers,
    # one for each actual contents of the array, then one for the entire nums1 which is of
    # m + n length. from there, we need to check that per iteration.

    # if the value at ptr1 is greater than the value at ptr1, then we will set the value
    # at ptr1 to the value at ptr3 and decrement ptr1. 
    # else, we will set the value at ptr2 to the value at ptr3, and decrement ptr2.

    # then we need to handle the edge case where there are still values in ptr2, 
    # with this we just do while ptr2 >= 0, and set the value at ptr3 to the value at ptr2
    # then decrement ptr2 and ptr3.
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return
        
        if m == 0:
            nums1[:] = nums2
            return
        
        ptr1 = m - 1
        ptr2 = n - 1
        ptr3 = m + n - 1

        while ptr2 >= 0 and ptr1 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptr3] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr3] = nums2[ptr2]
                ptr2 -= 1
            
            ptr3 -= 1
        
        while ptr2 >= 0:
            nums1[ptr3] = nums2[ptr2]
            ptr2 -= 1
            ptr3 -= 1
        
        
        return 

