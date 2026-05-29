// Chapter 7.0 — Recursion patterns: linear, tree, and divide-and-conquer
#include <vector>
#include <unordered_map>

class Solution {
public:
    // Shape 1: linear recursion. C++ compilers may optimize tail calls under
    // -O2, but the standard does not require it; treat as Theta(n) stack.
    long long fibLinear(int n) { return fibLinearAcc(n, 0LL, 1LL); }

    // Shape 2: tree recursion. Exponential without a cache.
    long long fibTree(int n) {
        if (n < 2) return n;
        return fibTree(n - 1) + fibTree(n - 2);
    }

    // Shape 2 + memo. Theta(n) total work, Theta(n) cache + stack.
    long long fibMemo(int n) {
        std::unordered_map<int, long long> cache;
        return fibMemoHelper(n, cache);
    }

    // Canonical entrypoint.
    long long fib(int n) { return fibMemo(n); }

    // Shape 3: divide-and-conquer. T(n) = 2T(n/2) + Theta(n).
    std::vector<int> mergeSort(const std::vector<int>& nums) {
        if (nums.size() <= 1) return nums;
        std::size_t mid = nums.size() / 2;
        std::vector<int> left(nums.begin(), nums.begin() + mid);
        std::vector<int> right(nums.begin() + mid, nums.end());
        return merge(mergeSort(left), mergeSort(right));
    }

private:
    long long fibLinearAcc(int n, long long a, long long b) {
        if (n == 0) return a;
        return fibLinearAcc(n - 1, b, a + b);
    }

    long long fibMemoHelper(int n, std::unordered_map<int, long long>& cache) {
        if (n < 2) return n;
        auto it = cache.find(n);
        if (it != cache.end()) return it->second;
        long long ans = fibMemoHelper(n - 1, cache) + fibMemoHelper(n - 2, cache);
        cache[n] = ans;
        return ans;
    }

    std::vector<int> merge(const std::vector<int>& a, const std::vector<int>& b) {
        std::vector<int> out;
        out.reserve(a.size() + b.size());
        std::size_t i = 0, j = 0;
        while (i < a.size() && j < b.size()) {
            if (a[i] <= b[j]) out.push_back(a[i++]);
            else              out.push_back(b[j++]);
        }
        while (i < a.size()) out.push_back(a[i++]);
        while (j < b.size()) out.push_back(b[j++]);
        return out;
    }
};
