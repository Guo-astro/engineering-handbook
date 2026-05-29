// LC 1046. Last Stone Weight
#include <queue>
#include <vector>

class Solution {
public:
    int lastStoneWeight(std::vector<int>& stones) {
        // C++ std::priority_queue defaults to max-heap on < — what we want here.
        std::priority_queue<int> heap(stones.begin(), stones.end());
        while (heap.size() > 1) {
            int y = heap.top(); heap.pop(); // heaviest
            int x = heap.top(); heap.pop(); // second heaviest
            if (y != x) heap.push(y - x);
        }
        return heap.empty() ? 0 : heap.top();
    }
};
