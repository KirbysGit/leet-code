# https://leetcode.com/problems/reverse-nodes-in-k-group/
# hard

class planningOut:

    # 02 / 20 / 2026 - 3:38 pm

    # the way i'm looking at it right now is like we do the copy approach while iterating
    # through list. 

    # so like what we did in the last problem #92. where we copy the nodes assuming
    # the indexes are like in the pairing of 2's. then if its the case that is less than
    # k amount, then we just don't change it. 

    # but basically like loop through, doing like while (k) then resetting at every 
    # k amount. then basically change the nodes to the new copied group. 

class holyShit:

    # 02 / 25 / 2026 - 11:39 pm

    # i mean bro looking at the problem it doesn't seem that bad, but it gets so weird
    # with the hand off from one group of k nodes to the next.

    # like here is where i am right now : 

    # idea is first set up some basics before loop :

    # head = front
    # (1) -> (2) -> (3) -> (4) -> (5) -> None

    # begin
    # (0) -> None

    # copy = end
    # (0)

    # then i want to create copies that reverse the list, then connect them. but i'm having trouble with connecting.

    # i gotta draw it out more. i spent a while so far. need to plan it out more i guess.

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        idx = 0
        front = head
        begin = ListNode(0)
        begin.next = None
        copy = ListNode(0)
        end = copy

        while head is not None:
            start = copy
            while idx < k and head is not None:
                copy.val = head.val
                tmp = ListNode(0)
                prev = copy
                copy = tmp
                copy.next = prev
                head = head.next
                idx += 1
            if k == idx:
                start.next = head
                xtra = prev
                if begin.next == None:
                    begin.next = xtra
                end.next = prev
                copy = ListNode(0)
                idx = 0
                
        return begin.next