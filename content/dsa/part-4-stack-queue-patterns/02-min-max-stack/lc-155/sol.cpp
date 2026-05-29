// LC 155. Min Stack
#include <algorithm>
#include <stack>

namespace dsa {

class MinStack {
public:
    MinStack() = default;

    void push(int val) {
        values_.push(val);
        int current = mins_.empty() ? val : std::min(mins_.top(), val);
        mins_.push(current);
    }

    void pop() {
        values_.pop();
        mins_.pop();
    }

    int top() const { return values_.top(); }
    int getMin() const { return mins_.top(); }

private:
    std::stack<int> values_;
    std::stack<int> mins_;
};

}  // namespace dsa
