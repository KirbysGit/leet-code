# https://leetcode.com/problems/daily-temperatures/
# medium

class firstAttempt:

    # 11 / 14 / 2025 - 2:10 pm

    # Did not work.

    # Too slow, but I think I had the right approach in general. 
    # Worked for some of the cases, except time limit exceeded.

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        start, days, idx = 0, 1, 1
        res = []

        while start < n:
            if idx >= n:
                res.append(0)
                start += 1
                idx = start + 1
                days = 1
                continue
            
            if temperatures[start] < temperatures[idx]:
                res.append(days)
                start += 1
                idx = start + 1
                days = 1
                continue
            
            days += 1
            idx += 1
        
        return res

class correct:

    # 11 / 14 / 2025 - 2:17 pm

    # Runtime -> 90 ms - 72.83%
    # Memory -> 27.40 MB - 73.53%

    # this approach uses a monotonic stack to keep track of temperatures.

    # basically, we have the same earlier set up but with a stack.

    # and now we enumerate through our temperatures list, and for each temperature,
    # we check if current temp is greater than the temperature at the index stored
    # at the top of the stack, if so, we pop the index from the stack and set the 
    # index to the current index minus the index popped from the stack, then
    # we append the current index to the stack.

    # simplified explanation :

    # for each day, while today's temp is warmer than the last day stored in the stack,
    # we pop that day off the stack and record how many days it took to get warmer (cur_index - popped_index)
    # then we add today's index to the stack to wait for its own warmer day.
    
    # def a little confusing. but im getting it.

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res