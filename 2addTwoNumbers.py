# https://leetcode.com/problems/add-two-numbers/
# medium

class firstAttempt:

    # 11 / 17 / 2025 - 2:57 pm

    # Runtime -> 7 ms - 32.76%
    # Memory -> 17.73 MB - 84.63%

    # alright so for this problem, i had the right approach after i cleared out whatever the
    # fuck i was thinking before. like i for some reason was like "NO I NEED TO REVERSE THE LIST"
    # because i thought the carry moved backwards, but nope!

    # once i realized that, it was a pretty simple ideology, add, check if it goes over 10, if so
    # bring the carry over, then re-sum and continue again.

    # my main issue was setting up the list to store the final vals in, just forgot how to initialize 
    # it, and also handling the NoneType errors, like in a case where the two lists are not the 
    # same length you need to make sure that you can handle the overlap well. so it was really just
    # a series of extra if statements. 

    # but anyways, update add1 per iteration, and continue with adding and then setting the value in
    # the list. pretty simple overall approach.

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        final = ListNode()
        tmp = final

        add1 = 0

        while l1 or l2 or add1:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            val = val1 + val2 + add1
            add1 = val // 10
            val %= 10

            tmp.val = val
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            if l1 or l2 or add1:
                tmp.next = ListNode()
                tmp = tmp.next

        return final