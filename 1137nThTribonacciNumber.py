# https://leetcode.com/problems/n-th-tribonacci-number/
# easy

class firstAttempt:

    # 10 / 29 / 2025 - 1:14 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 17.60 MB - 95.70%

    # really simple, i looked at the hints for the problem in the bottom
    # section of the leetcode and it said to declare an array of length n + 1, 
    # and i literally thought it just wanted us to declare the array with the 
    # answers and i was so confused.

    # but then i realized you just fill up the array with the tribonacci sequence
    # yourself, the array is just the placeholder as the values only go up to 37
    # in the problem constraints.
    
    # pretty simple tho, declare array of 38, set first 3 values, then iterate through
    # array, setting current idx to th sum of the previous 3 values, then
    # return the value at index n.

    def tribonacci(self, n: int) -> int:
        
        F = [0] * 38
        F[1] = F[2] = 1

        idx = 3
        while idx <= n:
            F[idx] = F[idx - 1] + F[idx - 2] + F[idx - 3]
            idx+=1

        return F[n]