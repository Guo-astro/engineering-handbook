// LC 509. Fibonacci Number
#include <unordered_map>

class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;
        auto it = memo.find(n);
        if (it != memo.end()) return it->second;
        int v = fib(n - 1) + fib(n - 2);
        memo[n] = v;
        return v;
    }
private:
    std::unordered_map<int, int> memo;
};
