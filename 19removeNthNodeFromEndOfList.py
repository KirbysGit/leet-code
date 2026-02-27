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
        