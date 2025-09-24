# https://leetcode.com/problems/number-of-recent-calls/
# easy

class firstAttempt:

    # 09 / 24 / 2025 - 3:10 PM

    # Runtime -> 40 ms - 56.86%
    # Memory -> 23.06 MB - 75.64%

    # no chatgpt used!!

    # set up a list to store the calls in init()
    def __init__(self):
        self.recent_requests = []

    # now in here, first add call to this list
    # then we set a minT value to be current time - 3000
    # then iterate through list, if call is great than minT we break
    # else we pop from the list

    # then return the length of the list

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)
        
        minT = t - 3000

        idx = 0

        while (idx < len(self.recent_requests)):
            if self.recent_requests[idx] >= minT:
                break
            
            self.recent_requests.pop(0)

        return len(self.recent_requests)