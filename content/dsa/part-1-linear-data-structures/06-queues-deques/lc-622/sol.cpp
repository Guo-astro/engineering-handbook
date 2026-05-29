// LC 622. Design Circular Queue
// Fixed-capacity ring buffer. head and tail advance modulo cap; an explicit
// count distinguishes empty (count == 0) from full (count == cap), which
// pure modular indexing alone cannot. All operations O(1), O(k) space.
#include <vector>

class MyCircularQueue {
public:
    MyCircularQueue(int k) : buf_(k), cap_(k), head_(0), tail_(0), count_(0) {}

    bool enQueue(int value) {
        if (count_ == cap_) return false;
        buf_[tail_] = value;
        tail_ = (tail_ + 1) % cap_;
        ++count_;
        return true;
    }

    bool deQueue() {
        if (count_ == 0) return false;
        head_ = (head_ + 1) % cap_;
        --count_;
        return true;
    }

    int Front() const { return count_ == 0 ? -1 : buf_[head_]; }
    // Add cap before mod to keep the result non-negative when tail_ == 0.
    int Rear()  const { return count_ == 0 ? -1 : buf_[(tail_ - 1 + cap_) % cap_]; }
    bool isEmpty() const { return count_ == 0; }
    bool isFull()  const { return count_ == cap_; }

private:
    std::vector<int> buf_;
    int cap_;
    int head_;
    int tail_;
    int count_;
};
