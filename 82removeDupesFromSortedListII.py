# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# medium

class firstAttempt:

    # 03 / 01 / 2026 - 11:43 pm

    # need to get a git push, worked on this a bit but now working on tizi site and
    # don't want to push as its to vercel right now.

    # so im throwing my progress in here, i'll finish it soon, its pretty simple 
    # just need to think about it.

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        front = head
        seen = {}

        while front != None:
            seen[front.val] = seen.get(front.val, 0) + 1
            front = front.next

        before = ListNode(0)
        start = ListNode(-1)
        before.next = start

        front = head

        while front != None:
            if seen[front.val] == 1:
                start.val = front.val
                start.next = ListNode(0)
                start = start.next

            front = front.next
        
        start = None
        
        print(before)


class working:

    # 03 / 02 / 2026 - 1:31 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.32 MB - 66.88%

    # i rearranged the front != None set up from the previous point, where it just skips
    # if the freq array value is greater than 1. so it only continues the list if the value 
    # is 1. 

    # i think this can be done without the hash map so i want to try that.

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        front = head
        seen = {}

        while front != None:
            seen[front.val] = seen.get(front.val, 0) + 1
            front = front.next

        before = ListNode(0)
        start = before

        front = head

        while front != None:
            while front and seen[front.val] != 1:
                front = front.next

            if front == None:
                start.next = None
                break
            
            start.next = front
            start = start.next
            front = front.next
    
        return before.next

class simpler:

    # 03 / 02 / 2026 - 2:31 pm

    # same runtime.

    # alright but this oen appears simpler, what it does is basically the same sort of
    # thing i was trying to do without the freq but i couldn't understand how to properly
    # skip but also handle like not over-skipping leaving the values misaligned for like comparison.

    # what this does is the basic :

    # create a dummy node to point to the head we can return for later.
    # use a prev pointer to allow us to skip over duplicates.

    # while the pointer is not none, if the cur value is same as next value, skip over all dupes.
    # then check if the prev pointer is pointing to the cur pointer, if it is not, then we know that there
    # was some duplicates, so we adjust the prev pointer to the next pointer after the cur pointer.

    # and just update the curr pointer as we move through the list.

    # this will get rid of all duplicates, and preserve the original list structure, and all
    # we have to do is return the next node after dummy.

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head
        dummy = ListNode(0,head)
        prev = dummy

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            
            if prev.next == curr:  
                prev = prev.next
            
            else: 
                prev.next = curr.next
            curr = curr.next

        return dummy.next
