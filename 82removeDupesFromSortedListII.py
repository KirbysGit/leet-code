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
class Solution:
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


