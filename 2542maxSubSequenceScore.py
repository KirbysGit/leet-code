# https://leetcode.com/problems/maximum-subsequence-score/
# medium

class firstAttempt:

    # 10 / 21 / 2025 - 1:42 pm

    # Runtime - 177 ms - 69.80%
    # Memory - 40.26 MB - 56.94%

    # the key is to reverse sort the nums2, and then use a minheap to keep track of nums1.

    # start off, by zipping two list together, sorting reverse based on nums2.

    # initialize some values, a heap and max and cur score.

    # then iterate through the pairs, adding the num1 to the heap and the cur score,
    # only if the heap is less than k, then we will continuously add to the heap,
    # then if the heap is greater than k, we will pop smallest value, then 
    # subtract it from the cur score, then if the heap is equal to k, we will,
    # check to see if the cur score is greater than the max score, if so
    # update the max score.

    # main secret is reversing the list so we don't have to go through every
    # single permutation of the subsequences.

    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # here was my initial thought : (pretty far off honestly)
        
        # im thinking like in terms of multiplication will be the strongest suit 
        # for any sort of value, like the majority of the value will come
        # from the multiplication, so priorizting which is the highest value, then k - 1 indexes
        # down from there. then just taking the accordining indices from num1.

        # thats all i got right now.

        # go through nums 2, create like a max-value -> index dict or something so we
        # can track the proper according idx.

        # or maybe combining them into a dict where the key is the nums2, then sort based on that,
        # then just take the min of the k values, then if multiple are the same, go through with 
        # then max set up of the nums1.


        pairs = list(zip(nums2, nums1))

        pairs.sort(reverse=True)

        heap = []

        max_score = cur_score = 0


        for num2, num1 in pairs:
            cur_score += num1
            heappush(heap, num1)
            if len(heap) > k:
                cur_score -= heappop(heap)
            if len(heap) == k:
                max_score = max(max_score, cur_score * num2)
                
        return max_score