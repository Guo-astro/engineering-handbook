// LC 232. Implement Queue using Stacks
#include <stack>

namespace dsa {

// FIFO via two LIFO stacks. Both pop and peek are non-const because the
// internal inbox/outbox split mutates on transfer, even though the queue's
// observable contents do not.
class MyQueue {
public:
    MyQueue() = default;

    void push(int x) {
        inbox_.push(x);                    // O(1) always
    }

    int pop() {
        if (outbox_.empty()) transfer();
        int v = outbox_.top();
        outbox_.pop();
        return v;                          // O(1) amortized
    }

    int peek() {
        if (outbox_.empty()) transfer();
        return outbox_.top();              // O(1) amortized
    }

    bool empty() const {
        return inbox_.empty() && outbox_.empty();
    }

private:
    void transfer() {
        while (!inbox_.empty()) {
            outbox_.push(inbox_.top());
            inbox_.pop();
        }
    }

    std::stack<int> inbox_;
    std::stack<int> outbox_;
};

}  // namespace dsa
