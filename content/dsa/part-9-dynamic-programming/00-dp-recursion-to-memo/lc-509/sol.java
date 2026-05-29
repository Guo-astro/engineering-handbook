// LC 509. Fibonacci Number
import java.util.HashMap;
import java.util.Map;

class Solution {
    private final Map<Integer, Integer> memo = new HashMap<>();

    public int fib(int n) {
        if (n < 2) return n;
        Integer cached = memo.get(n);
        if (cached != null) return cached;
        int v = fib(n - 1) + fib(n - 2);
        memo.put(n, v);
        return v;
    }
}
