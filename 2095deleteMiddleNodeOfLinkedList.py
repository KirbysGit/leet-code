# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# medium

class firstAttempt:

    # 09 / 26 / 2025 - 3:38 pm

    # Runtime -> 43 ms - 91.41%
    # Memory -> 48.98 MB - 52.43%

    # had to use chatGPt because I didn't understand how head actually was being changed
    # i tried one attempt but I want adjusting head that it wasn't really working to 
    # return the right value because i was adjusting head but i didn't even realize.

    # but anyways, it gave me some hints, the double pointer with fast and slow is 
    # something i've definitely seen before, but it makes sense. as we just iterate
    # the fast two steps, and the slow one just one step, then keep track of the prev
    # for the sake of deleting at the end, and we just move the pointer over not even
    # really delete it, then return the head.
    
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            prevSlow = slow
            slow = slow.next
        
        prevSlow.next = slow.next

        return head