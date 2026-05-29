// LC 21. Merge Two Sorted Lists
public final class Sol {

    public static final class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    /** Iterative dummy-node + tail-pointer merge.
     *  Stable: l1 wins on ties (`<=` not `<`). O(n + m) time, O(1) space. */
    public ListNode mergeTwoListsIterative(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);  // sentinel; never returned.
        ListNode tail = dummy;             // invariant: tail is last spliced node.
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {        // `<=` keeps stability: l1 wins on tie.
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        tail.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }

    /** Textbook recursive form. O(n + m) JVM stack; prefer iterative. */
    public ListNode mergeTwoListsRecursive(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        if (l1.val <= l2.val) {
            l1.next = mergeTwoListsRecursive(l1.next, l2);
            return l1;
        }
        l2.next = mergeTwoListsRecursive(l1, l2.next);
        return l2;
    }
}
