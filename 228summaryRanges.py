# https://leetcode.com/problems/summary-ranges/
# easy

class firstAttempt:

    # 01 / 27 / 2026 - 12:22 am

    # working on it.

    # servers are down so im just going to leave this here.

    def summaryRanges(self, nums: List[int]) -> List[str]:

        out = []

        start = nums[0]
        end = nums[0]
                
        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1] + 1:
                if start == end:
                    out.append(f"{end}")
                else:
                    out.append(f"{start}->{end}")
                
                start = nums[idx]
                end = nums[idx]
            else:
                end = nums[idx - 1]

        return out
            
class correct:

    # 01 / 27 / 2026 - 1:51 pm

    # alright i was working on this all of last night and really wasn't fare off, i just
    # wasn't really paying attention to where the code was going wrong. becuase i was
    # using the sort of "idx - 1" or "idx + 1" to check the values in the array, i was
    # usually missing at least one.

    # like for the example : 

    # input -> [0,2,3,4,6,8,9]

    # i was missing the 8,9 at the end. so i just had to literally had the extra check
    # you'll see below and it worked. i was going back and forth though on like what i 
    # was doing wrong because i was 100% sure it should've worked, and technically i 
    # was right there i just had to change it a tiny bit.

    # here's the code below,
    # basically like if prev value + 1 is current value, update end value, else
    # handle adding the start and end to output array.

    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0: 
            return []

        out = []

        start = nums[0]
        end = nums[0]
                
        for idx in range(1, len(nums)):
            if nums[idx] == end + 1:
                end = nums[idx]
            else:
                if start == end:
                    out.append(f"{end}")
                else:
                    out.append(f"{start}->{end}")
                
                start = nums[idx]
                end = start
        
        if start == end:
            out.append(f"{end}")
        else:
            out.append(f"{start}->{end}")

        return out