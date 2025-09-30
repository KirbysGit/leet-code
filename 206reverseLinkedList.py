# https://leetcode.com/problems/reverse-linked-list/
# easy

class firstAttempt:

    # 09 / 27 / 2025 - 2:20 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 18.46 MB - 95.72%

    # all by myself!!

    # took me a fat minute, but i got it, this is the set up.

    # if list is empty or has one node, just return that head.
    # if list has two nodes, just reverse them and return new head.
    
    # else,
    # we're working through with our prev, start, and new pointers.
    # we start out by basically just incrementing through the list with start and new,
    # basically pointing each node to the previous one, then eventually just returning
    # the new head. 

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        prev = None
        start = head
        new = head.next
        
        if head.next.next is None:
            start.next = prev
            new.next = start
            return new

        while start and new and new.next:
            tmp = new.next
            start.next = prev
            new.next = start

            prev = start
            start = new
            new = tmp

        new.next = start

        return new
