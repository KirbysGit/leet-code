# https://leetcode.com/problems/linked-list-cycle/
# easy

class firstAttempt:

    # 02 / 13 / 2026 - 1:41 pm

    # Runtime -> 54 ms - 41.27%
    # Memory -> 22.50 MB - 65.22%

    # i really couldn't figure this out, like you can't check membership of values,
    # you can't track idx's.

    # i just went with the easy approach kind of taking advantage of one of the 
    # constraints which is the list will be no more than 10000 nodes. so if the count
    # ever goes above that then we know there's a cycle.

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        front = head
        idx = 0

        while front and front.next:
            if idx > 10000:
                return True
            else:
                idx += 1
                front = front.next
        
        return False

class secondAttempt:

    # 02 / 13 / 2026 - 2:31 pm

    # Runtime -> 52 ms - 52.72%
    # Memory -> 22.79 MB - 19.77%

    # alright this one i don't know if i really would've thought of but it
    # makes sense in hindsight.

    # the idea is to use a fast and slow pointer. where fast moves two steps
    # and slow moves one step. if there's a cycle, then fast and slow will
    # eventually meet. 

    # i wasn't really understanding how they eventually meet, like is there
    # not a case that the fast pointer goes behind the slow point and just stays
    # like perfectly "parallel" with it in some sense.

    # but thinking about it, if the loop is infinite, then the fast pointer will
    # definitely have to overlap at some point.

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is None or slow is None:
                return False
            if slow == fast:
                return True