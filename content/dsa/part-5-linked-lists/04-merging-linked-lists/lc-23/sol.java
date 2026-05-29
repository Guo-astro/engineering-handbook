// LC 23. Merge k Sorted Lists
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public final class Sol {

    public static final class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    /** Min-heap of (val, listIndex). int[] avoids PriorityQueue<Integer>
     *  boxing; comparingInt(...).thenComparingInt(...) is overflow-safe.
     *  O(N log k) time, O(k) auxiliary. */
    public ListNode mergeKListsHeap(ListNode[] lists) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                Comparator.<int[]>comparingInt(a -> a[0])
                        .thenComparingInt(a -> a[1]));
        ListNode[] cursors = (lists == null) ? new ListNode[0] : lists.clone();
        for (int i = 0; i < cursors.length; i++) {
            if (cursors[i] != null) {
                pq.offer(new int[]{cursors[i].val, i});
            }
        }
        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            int idx = top[1];
            ListNode node = cursors[idx];
            tail.next = node;
            tail = tail.next;
            cursors[idx] = node.next;
            if (cursors[idx] != null) {
                pq.offer(new int[]{cursors[idx].val, idx});
            }
        }
        tail.next = null;
        return dummy.next;
    }

    /** Pairwise divide-and-conquer. log k merge levels, O(N) work per
     *  level. O(N log k) time, O(log k) recursion stack. */
    public ListNode mergeKListsDivideConquer(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        List<ListNode> current = new ArrayList<>();
        for (ListNode head : lists) current.add(head);
        while (current.size() > 1) {
            List<ListNode> merged = new ArrayList<>();
            for (int i = 0; i < current.size(); i += 2) {
                ListNode a = current.get(i);
                ListNode b = (i + 1 < current.size()) ? current.get(i + 1) : null;
                merged.add(mergeTwo(a, b));
            }
            current = merged;
        }
        return current.get(0);
    }

    /** LC 21's iterative merge, used as the leaf step of d-and-c. */
    private ListNode mergeTwo(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (a != null && b != null) {
            if (a.val <= b.val) {
                tail.next = a;
                a = a.next;
            } else {
                tail.next = b;
                b = b.next;
            }
            tail = tail.next;
        }
        tail.next = (a != null) ? a : b;
        return dummy.next;
    }
}
