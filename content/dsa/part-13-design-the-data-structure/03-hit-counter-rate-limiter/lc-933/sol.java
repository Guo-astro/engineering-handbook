// LC 933. Number of Recent Calls
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {

    static class RecentCounter {
        // ArrayDeque is the canonical Java deque per the code-idioms contract;
        // LinkedList and the legacy Stack class are forbidden.
        private final Deque<Integer> q = new ArrayDeque<>();

        public int ping(int t) {
            q.addLast(t);
            // Strict `<`: q.peekFirst == t - 3000 is INSIDE the window.
            while (!q.isEmpty() && q.peekFirst() < t - 3000) {
                q.pollFirst();
            }
            return q.size();
        }
    }

    private Sol() {}
}
