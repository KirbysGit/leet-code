# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# medium

class firstAttempt:

    # 02 / 27 / 2026 - 4:20 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.24 MB - 81.02%

    # alright i worked through this completely set on like "oh i just gotta remove the nth node in the list",
    # but i read the question wrong, it was actually the nth not from the END of the list.

    # so from there i was like, damn can i do this in like one pass? but i didn't really know how to do that,
    # maybe with a fast and slow pointer, but like idk that was overly complex in my brain.

    # so instead i just walked the list once to get the length.
    
    # then after walking, we knew what index to remove by subtracting n from length,
    # and from there we just walked the list again until we go the index to remove.

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        idx = 0
        front = head
        prev = head
        length = 0 

        while head != None:
            head = head.next
            length += 1

        head = front

        while idx != length - n:
            prev = head
            head = head.next
            idx += 1

        prev.next = head.next

        if idx != 0:
            return front
        else:
            return head.next
        
class fastSlow:

    # 02 / 28 / 2026 - 4:55 pm

    # i guess it can be done with fast and slow pointers. i was looking at the
    # fastest solution, and i was like i don't get how it could be done, because
    # the pointer would kind of just overlap? or like you couldn't really get an exact
    # point of stopping. but i guess it works!

    # this idea is still a little blurry in my head, but what its doing is basically
    # moving the fast pointer n steps ahead from the slow pointer. so when we start
    # iterating through and the fast pointer reaches the end of hte list the slow pointer
    # will be at the node to remove (the nth node from the end), so we just "remove" it
    # by pointing the prev to the next around the to be deleted node, and return the head!

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        slow=head
        for _ in range(n):
            fast=fast.next
        if not fast: return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head