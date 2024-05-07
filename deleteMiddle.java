class deleteMiddle {
    // First Attempt... 05 / 07 / 2024 - 6:33 pm
    // Count Length of List.
    // Take Length and find Mid from that.
    // Iterate through until Mid - 1.
    // Save Node.
    // When Mid, Delete Connection and Swap to Rest.
    // Else, Iterate through List.
    // RT - 24.04%, MEM - 79.63%
    public ListNode deleteMiddleFirst(ListNode head) {
        if (head == null || head.next == null) return null;

        ListNode cur = head;
        int counter = 0;

        while (cur != null) {
            counter++;
            cur = cur.next;
        }

        int middle = counter / 2;
        ListNode prev = head;
        cur = head;

        for (int i = 0; i < counter; i++) {
            if (i == middle - 1) {
                prev = cur;
                cur = cur.next;
            } else if (i == middle) {
                prev.next = cur.next;
                cur.next = null;
                cur = prev.next;
            } else {
                cur = cur.next;
            }
        }

        return head;
    }
}
