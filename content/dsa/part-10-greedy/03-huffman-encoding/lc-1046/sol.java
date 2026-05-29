// LC 1046. Last Stone Weight
import java.util.PriorityQueue;
import java.util.Collections;

public class Sol {
    public int lastStoneWeight(int[] stones) {
        // Java PriorityQueue defaults to min-heap; reverseOrder gives max-heap.
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : stones) heap.offer(s);
        while (heap.size() > 1) {
            int y = heap.poll(); // heaviest
            int x = heap.poll(); // second heaviest
            if (y != x) heap.offer(y - x);
        }
        return heap.isEmpty() ? 0 : heap.poll();
    }
}
