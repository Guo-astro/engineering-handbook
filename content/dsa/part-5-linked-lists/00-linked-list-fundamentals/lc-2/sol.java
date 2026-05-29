// LC 2. Add Two Numbers
// Synchronized two-list walk with carry propagation. The dummy head
// lets every iteration append unconditionally; `return dummy.next`
// skips the sentinel.
public final class Sol {

    public static final class ListNode {
        public int val;
        public ListNode next;
        public ListNode() {}
        public ListNode(int val) { this.val = val; }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int v1 = (l1 != null) ? l1.val : 0;
            int v2 = (l2 != null) ? l2.val : 0;
            int total = v1 + v2 + carry;
            carry = total / 10;
            tail.next = new ListNode(total % 10);
            tail = tail.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        return dummy.next;
    }
}
