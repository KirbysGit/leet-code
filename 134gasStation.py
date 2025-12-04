# https://leetcode.com/problems/gas-station/
# medium

class firstAttempt:

    # im really tired dude i'll come back to this tmrw to review how to do it.

    # 12 / 03 / 11:35 pm 

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