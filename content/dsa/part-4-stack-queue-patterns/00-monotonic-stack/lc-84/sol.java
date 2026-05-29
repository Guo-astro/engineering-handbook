// LC 84. Largest Rectangle in Histogram
import java.util.ArrayDeque;
import java.util.Deque;

public final class Sol {
    public int largestRectangleArea(int[] heights) {
        int ans = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        int n = heights.length;
        for (int i = 0; i <= n; i++) {
            int cur = (i == n) ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > cur) {
                int h = heights[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                if (h * w > ans) {
                    ans = h * w;
                }
            }
            stack.push(i);
        }
        return ans;
    }
}
