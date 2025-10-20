# https://leetcode.com/problems/kth-largest-element-in-an-array/
# medium

class firstAttempt:

    # 10 / 20 / 2025 - 8:36 pm

    # Runtime -> 56 ms - 77.38%
    # Memory -> 28.91 MB - 15.90%

    # this one took me like two seconds, i assume its supposed to be harder for 
    # other languages but becasue python has the sort function it makes it easy.
    
    # but also i know there is probably a better way to do this, like i don't 
    # know what type of sorting algorithm is used in the sort() but i think
    # probably setting up a merge sort then returning the k-th element would be better.

    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort = sorted(nums)
        n = len(sort)
        return sort[n - k]