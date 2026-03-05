# https://leetcode.com/problems/partition-list/
# medium

class firstAttempt:

    # im the goat.

    # 03 / 05 / 2026 - 2:28 pm

    # this shit took me like 5 minutes. insane. I LOVE GETTING BETTER!!

    # oh yea 

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.27 MB - 90.55%

    # i don't really know if this is how they intended for us to do it
    # but it really is just like a sorting list problem. but i saw it and
    # was like, i just need to have access to the values and then just 
    # combine them based on the partition.

    # all i did was iterate through the linked list, adding the values
    # to the above list if they were greater than or equal to the partition
    # then if it was less than the partition, i added it to the below list.

    # so that way i preserve the original ordering of the list, then just combine
    # the list, and iterate through the list creating a new linked list
    # just setting the values to nodes, then return the head of that new list.

    # code :
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        front = head
        above = []
        below = []

        while front != None:
            if front.val >= x:
                above.append(front.val)
            else:
                below.append(front.val)

            front = front.next

        final = below + above

        prev = ListNode(0)
        start = prev

        for val in final:
            new = ListNode(val)
            prev.next = new
            prev = new
        
        return start.next
            
            
