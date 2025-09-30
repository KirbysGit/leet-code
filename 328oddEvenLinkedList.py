# https://leetcode.com/problems/odd-even-linked-list/
# medium

class firstAttempt:

    # 09 / 27 / 2025 - 1:33 pm

    # Runtime -> 0 ms - 100.00%
    # Memory -> 19.13 MB - 74.02%

    # no chatgpt just had to think through, originally was trying to solve it 
    # kind of with a brute force method but there was limits on runtime so i knew
    # it could only be solved with one pass through the list

    # what i landed on was kind of similar to the fast and slow pointer approach,
    # except its the same speed just separated by one idx, so we have odd as the first
    # idx and even as the second, and we keep track of the evenHead for later connection
    # but we iterate through list, setting the next of odd to the next next node and same
    # for even, but then we connect the end of the odd list to the evenHead and return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = head.next

        while odd and even and odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = evenHead
        return head