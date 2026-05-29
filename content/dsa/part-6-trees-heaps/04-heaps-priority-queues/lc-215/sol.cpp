// LC 215. Kth Largest Element in an Array
// heap solution mirrors.
// std::priority_queue is max-heap by default; pass std::greater<int> for min-heap.
#include <queue>
#include <vector>
#include <functional>

class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> heap;
        for (int x : nums) {
            if ((int)heap.size() < k) {
                heap.push(x);
            } else if (x > heap.top()) {
                heap.pop();
                heap.push(x);
            }
        }
        return heap.top();
    }
};
