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

class imBack:

    # 02 / 14 / 2026 - 3:38 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.25 MB - 64.84%

    # im the goat!!!!

    # looking at the last attempt and looking at this one. i've grown bro!!
    # i understand it better now, the approach was pretty easy, first attempt
    # here though i wasn't considering the values adding up over 10, so i needed
    # to handle that as well as a carry variable to carry the value over.

    # my code is highkey kind of messy, but it works well!

    # i was just like lets check if l1 and l2 exist, if so add them both,
    # if not just add if either l1 or l2 as we know one of them will exist
    # based on the set up of the while loop.

    # then deal with if the value goes over 10, then handle the carry value
    # then update the values to the next in the list, then handle adding
    # a new node if both next steps are not none or carry > 0.

    # bam!!! im goated!

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        front = head
        carry = 0

        while l1 or l2 or carry > 0:
            if l1 is None and l2 is None and carry > 0:
                head.val = carry
                break

            if l1 and l2:
                head.val = l1.val + l2.val + carry
            elif l1:
                head.val = l1.val + carry
            elif l2:
                head.val = l2.val + carry

            carry = 0
            
            if head.val >= 10:
                carry = 1
                head.val = head.val % 10
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if l1 or l2 or carry > 0:
                step = ListNode()
                head.next = step
                head = head.next
        
        return front