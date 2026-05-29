// LC 295. Find Median from Data Stream
// std::priority_queue<int> is max-heap; std::greater<int> gives min-heap.
#include <queue>
#include <vector>
#include <functional>

class MedianFinder {
public:
    void addNum(int num) {
        lower_.push(num);
        upper_.push(lower_.top()); lower_.pop();        // ordering invariant
        if (upper_.size() > lower_.size()) {
            lower_.push(upper_.top()); upper_.pop();    // size invariant
        }
    }

    double findMedian() const {
        if (lower_.size() > upper_.size()) {
            return lower_.top();
        }
        return (lower_.top() + upper_.top()) / 2.0;     // float division
    }

private:
    std::priority_queue<int> lower_;                                       // max-heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> upper_;  // min-heap
};
