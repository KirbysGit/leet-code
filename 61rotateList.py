# https://leetcode.com/problems/rotate-list/
# medium

class firstAttempt:

    # 03 / 03 / 2026 - 2:28 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.32 MB - 70.52%

    # alright so my thought process while reading the problem was like
    # its pretty simple, because what we're doing is that we really
    # just need a way to figure out how to move the end node to the front
    # k times.

    # i was thinking about it that way, then i was like, ehh it gets kind of weird
    # with how we access the previous node, like we'd have to walk backwards but 
    # we really cant do that in a linked list unless we store everything.

    # so i was like, this is really just like a snippet problem, if we just 
    # add the back k nodes to the front, then point the last node before the
    # k to None, then it would work.

    # but i ran into some issues, like if k is over the amount of nodes i na list, so
    # i needed to modulo the lenght, but also the way i set it up, was like
    # if the k == 0, it gets offset, so i had to reorganize it.

    # but its basically the same as one of the earlier problems where i use the fast
    # and slow pointer to get like teh offset so when fast == None at the end then i know that slow
    # is at the kth node from the end. then from there just kind of take the snippet 
    # between teh slow and fast and point them to the right spots, so fast to head and slow to None.

    # then bam! and just had to do some small symptom handling earlier for edge cases.
    
    # little long, def can be simplified.

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        
        fast = head
        slow = head

        idx = 0

        while fast != None:
            fast = fast.next
            idx+=1

        if k % idx == 0:
            return head
        
        fast = head

        for _ in range(k % idx):
            fast = fast.next
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        start = slow.next
        fast.next = head
        slow.next = None

        return start