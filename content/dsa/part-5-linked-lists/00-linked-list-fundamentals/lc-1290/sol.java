// LC 1290. Convert Binary Number in a Linked List to Integer
// Single-pass walk with a running accumulator. Each node holds 0 or 1;
// shift the result left and OR in the current bit.
public final class Sol {

    public static final class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int val) { this.val = val; }
    }

    public int getDecimalValue(ListNode head) {
        int result = 0;
        ListNode curr = head;
        while (curr != null) {
            result = (result << 1) | curr.val;
            curr = curr.next;
        }
        return result;
    }
}
