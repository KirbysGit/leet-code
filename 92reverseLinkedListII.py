# https://leetcode.com/problems/reverse-linked-list-ii/
# medium

class firstAttempt:

    # 02 / 19 / 2026 - 12:54 am

    # i honestly had fun with this problem. like drawing it out was pretty sick
    # i think i just had such a hard time trying to visualize the way the connections
    # move that i gained a clarity after dumping it on my whiteboard.

    # took me the entire day tho if you couldn't tell by the timestamp.

    # worked on it for an hour before going to the range, another hour
    # after getting back from gym, then like 2 hours while i was eating dinner.

    # FIRE FIRE FIRE!!!!

    # IM THE GOATT!!!!!!

    # okay basically what i did, was like use the question from before to do copies.

    # the goal with it was to basically create a copy of the list while reversing it,
    # then connect the copy list into the original list based on the prev and next
    # value to the sublist. 

    # like for the first example, [1, 2, 3, 4, 5], we want to reverse the idx's from 2 to 4.
    # in my head i was like okay lets go like this, grab the [2, 3, 4] and reverse it while
    # grabbing it, then make the 1 point to 4, and 2 point to 5. and bam!!!

    # here's my code : 

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        front = head
        idx = 1
        cut = None
        
        copy = ListNode(0)
        prev = head

        # if we create a copy, like iterate through, reversing the copies
        # then we will be at end of list, can store the head aswell.

        while head != None:
            if idx == left:
                start = copy
                while idx <= right:
                    copy.val = head.val
                    tmp = ListNode(0)
                    cut = copy
                    copy = tmp
                    copy.next = cut
                    head = head.next
                    idx += 1
                prev.next = copy.next
                start.next = head
            else:
                prev = head
                head = head.next
                idx += 1


        return front if left != 1 else front.next

        # damn i was so excited i typed allat out in 3 minutes.