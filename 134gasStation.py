# https://leetcode.com/problems/gas-station/
# medium

class firstAttempt:

    # im really tired dude i'll come back to this tmrw to review how to do it.

    # 12 / 03 / 11:35 pm 

    # alright we're back!

    # 12 / 04 / 2025 - 3:11 pm

    # alright i get it now, pretty simple when you read it.
    # pretty crazy to break it down enough conceptually enough during the first attempt to understand it
    # can be done in one pass. i had the idea of just the total of gas but i shut it down because i thought ordering
    # would be necessary becasue you need to loop around and if like gas for one is 10, and then rest is like 1, 
    # then it would be impossible, but for the general check it would work just not the specific check i was trying to
    # approach with.
    
    # but anyways, we take the difference of gas and cost every index. we use this and add it to the total,
    # and to the current cost, then we check if current is < 0, because if so we can't start from that index as it
    # doesn't have enough gas to get to the nex index. so we update the start index to the next index if its less.
    # finally we check if the total is < 0 because if so then it's impossible to complete the circuit, else we 
    # return the last start index we had.

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        current = 0
        total = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            total += diff
            current += diff

            if current < 0:
                start = i + 1
                current = 0

        if total < 0:
            return -1
        else:
            return start