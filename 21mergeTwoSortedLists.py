# https://leetcode.com/problems/merge-two-sorted-lists/
# easy

class firstAttempt:

    # 02 / 15 / 2026 - 2:17 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.56 MB - 24.93%

    # alright so my approach is kind of brutal, its like the right mental
    # way to do it, but i definitely went a bit overboard with some of the conditions.

    # basically its just a two pointer sort of thing, check the values of each
    # of the node's that the lists are currently pointing to then add the
    # lower value to our main list and increment the pointer for that value to
    # the next until the list reach a none pointer where the other list will finish out
    # its list.

    # here's the code : 

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None

        final = ListNode()
        front = final
        
        while list1 or list2:

            v1 = list1.val if list1 else 101
            v2 = list2.val if list2 else 101

            if (v2 != 101 and v2 < v1) or v1 == 101:
                final.val = v2
                list2 = list2.next if list2.next else None
            elif (v1 != 101 and v2 >= v1) or v2 == 101:
                final.val = v1
                list1 = list1.next if list1.next else None
            else:
                break

            if list2 or list1:
                tmp = ListNode()
                final.next = tmp
                final = final.next

        return front


class secondAttempt:

    # 02 / 15 / 2026 - 9:38 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.36 MB - 52.76%

    # all i did was swap out the way i handled the 101 shit, like i felt that was 
    # stupid, because the only goal with that was to check like if the value existed
    # or not.

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None

        final = ListNode()
        front = final
        
        while list1 or list2:

            if list1 and list2:
                if  list2.val < list1.val:
                    final.val = list2.val
                    list2 = list2.next if list2.next else None
                elif list2.val >= list1.val:
                    final.val = list1.val
                    list1 = list1.next if list1.next else None
            elif list1:
                final.val = list1.val
                list1 = list1.next if list1.next else None
            elif list2:
                final.val = list2.val
                list2 = list2.next if list2.next else None
            else:
                break

            if list2 or list1:
                tmp = ListNode()
                final.next = tmp
                final = final.next

        return front

class soSmart:

    # just saw this.

    # same sort of run time.

    # 02 / 15 / 2026 - 9:45 pm

    # basically just iterates through as we do but instead of checking if
    # one of hte items exist to continue to loop, it does an AND check to
    # see if both exist so it saves time checking for like all the cases
    # that come with that nad just adds the remaining part of whichever list
    # if there is one.

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None

        final = ListNode()
        front = final
        
        while list1 and list2:

            if list2.val < list1.val:
                front.next = list2
                list2 = list2.next
            else:
                front.next = list1
                list1 = list1.next

            front = front.next

        front.next = list1 or list2

        return final.next