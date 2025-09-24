# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# easy

class firstAttempt:

    # 09 / 19 / 2025 - 2:39 pm

    # Runtime -> 3ms - 94.53%
    # Memory -> 18.33 MB - 22.25%

    # alright i had to use chatGPT just because i wanted to know if python had
    # specific stuff for hashmaps that made it easier, i knew the idea, but then 
    # again the hint chatgpt gave me basically just gave me the answer, 
    # i was thinking about tracking the frequency of each number in each array
    # then just checking if the number is in other array, if not add it to first result
    # so definitely would've been slower

    # but learning about the set() operation made it way easier. 

    # idea is really simple, convert to a set which gets rid of duplicates, then 
    # subtract the sets to get the difference, which returns a set with the 
    # values that are in the first set but not the second, and then vice versa,
    # and then just conver back to a list and return

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        onlyInNums1 = nums1Set - nums2Set
        onlyInNums2 = nums2Set - nums1Set

        return[list(onlyInNums1), list(onlyInNums2)]