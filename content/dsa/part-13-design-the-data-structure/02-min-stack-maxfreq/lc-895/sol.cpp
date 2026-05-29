// LC 895. Maximum Frequency Stack
// A pop returns the most-frequent element pushed so far, ties broken by
// recency. Two parallel hash maps: count[v] is v's current frequency;
// buckets[f] is the stack of values that have reached frequency f. A push
// at new count f appends to buckets[f] alone. A pop reads buckets[maxFreq],
// returning most-frequent + most-recent in one operation. O(1) per op.
#include <stack>
#include <unordered_map>

class FreqStack {
public:
    FreqStack() : maxFreq(0) {}

    void push(int val) {
        int f = ++count[val];
        buckets[f].push(val);
        if (f > maxFreq) maxFreq = f;
    }

    int pop() {
        int val = buckets[maxFreq].top();
        buckets[maxFreq].pop();
        --count[val];
        if (buckets[maxFreq].empty()) --maxFreq;
        return val;
    }

private:
    std::unordered_map<int, int> count;
    std::unordered_map<int, std::stack<int>> buckets;
    int maxFreq;
};
