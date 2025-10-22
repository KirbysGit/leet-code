# https://leetcode.com/problems/total-cost-to-hire-k-workers/
# medium

class firstAttempt:

    # 10 / 22 / 2025 - 1:38 pm

    # Runtime -> 98 ms - 90.46%
    # Memory -> 26.88 MB - 98.21%

    # these greedy problems are super hard to wrap my head around, its super easy
    # to understand in hindsight, but i need to train my brain to think like the simple way.

    # but anyways, the breakdown is greedy + heap + two pointer.

    # i had this first initial breakdown : 

        # costs - holds cost per candidate
        # k - number of workers
        # candidates - front and back idxs

        # so we need to have the array,
        # iterate through the values within candidates values of front and back - ?
        # check which of the values is the lowest or if the same, which idx is the earliest
        # pop that value, add it to total cost

        # potential issue - when values overlap, being able to save time? like list is 4
        # but candidates is 3, so front 3 and back 3, we're wasting 2 moves.

        # we're going to reference c for candidates

    # but that wasn't really a right approach, especially with how i went about the actual
    # implementation. but anyways, the true approach is like this ;

        # initialize two ptrs, left & right.
        # initialize two heaps, one for front x costs, and one for back x costs.
        # heapify! (i forgot to do this)
        # enter the loop, while we are looking for workers.
            # if leftHeap[0] has a lower value than rightHeap[0].
                # pop from leftHeap, add to totalCost, then add
                # the next unpicked cost, and increment left.
            # else.
                # do the inverse.

            # decrement k. 
        # return totalCost.

    # the main idea comes from the heap allowing us to just pop the smallest value out of
    # the potential candidates, then just add the next unpicked cost and not have to worry
    # about keeping track of the indexes, and just think about getting the smallest values
    # from the two heaps.

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        totalCost = 0

        l = candidates
        r = len(costs) - candidates - 1

        leftHeap = costs[:candidates]
        rightHeap = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)

        while k > 0:
            
            if not rightHeap or (leftHeap and leftHeap[0] <= rightHeap[0]):
                cost = heapq.heappop(leftHeap)
                totalCost += cost
                if l <= r:
                    heapq.heappush(leftHeap, costs[l])
                    l+=1
            else:
                cost = heapq.heappop(rightHeap)
                totalCost += cost
                if l <= r:
                    heapq.heappush(rightHeap, costs[r])
                    r -= 1

            k -= 1

        return totalCost

        