// LC 621. Task Scheduler
import java.util.*;

public class Solution {
    public int leastInterval(char[] tasks, int n) {
        if (n == 0) return tasks.length;
        int[] counts = new int[26];
        for (char t : tasks) counts[t - 'A']++;
        // PriorityQueue<Integer> autoboxes on every offer/poll; for production
        // hot-path use Eclipse Collections or fastutil.
        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());
        for (int c : counts) if (c > 0) heap.offer(c);
        Deque<int[]> cooldown = new ArrayDeque<>();  // {remaining, ready_time}
        int time = 0;
        while (!heap.isEmpty() || !cooldown.isEmpty()) {
            time++;
            if (!heap.isEmpty()) {
                int remaining = heap.poll() - 1;
                if (remaining > 0) {
                    cooldown.offerLast(new int[]{remaining, time + n});
                }
            }
            if (!cooldown.isEmpty() && cooldown.peekFirst()[1] == time) {
                heap.offer(cooldown.pollFirst()[0]);
            }
        }
        return time;
    }
}
