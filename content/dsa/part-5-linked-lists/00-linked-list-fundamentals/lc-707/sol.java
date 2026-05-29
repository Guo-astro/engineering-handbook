// LC 707. Design Linked List
/* Sentinel-driven singly linked list. The dummy head removes the
 * head-vs-mid case split: every insert and delete points at a
 * non-null predecessor `prev`, so the wiring is the same at index 0
 * and at index k.
 */
public final class Sol {

    private static final class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    private final ListNode dummy = new ListNode(0);
    private int length = 0;

    public Sol() {}

    public int get(int index) {
        if (index < 0 || index >= length) return -1;
        ListNode curr = dummy.next;
        for (int i = 0; i < index; i++) curr = curr.next;
        return curr.val;
    }

    public void addAtHead(int val) {
        addAtIndex(0, val);
    }

    public void addAtTail(int val) {
        addAtIndex(length, val);
    }

    public void addAtIndex(int index, int val) {
        if (index < 0 || index > length) return;
        ListNode prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;
        ListNode node = new ListNode(val);
        node.next = prev.next;
        prev.next = node;
        length++;
    }

    public void deleteAtIndex(int index) {
        if (index < 0 || index >= length) return;
        ListNode prev = dummy;
        for (int i = 0; i < index; i++) prev = prev.next;
        prev.next = prev.next.next;
        length--;
    }
}
