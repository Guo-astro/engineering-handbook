// LC 150. Evaluate Reverse Polish Notation
#include <cstdlib>
#include <stack>
#include <string>
#include <vector>

class Solution {
public:
    int evalRPN(const std::vector<std::string>& tokens) {
        std::stack<int> st;
        for (const auto& t : tokens) {
            if (t.size() == 1 && (t == "+" || t == "-" || t == "*" || t == "/")) {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                if      (t == "+") st.push(a + b);
                else if (t == "-") st.push(a - b);
                else if (t == "*") st.push(a * b);
                // C++11 onwards: integer division truncates toward zero.
                else               st.push(a / b);
            } else {
                st.push(std::atoi(t.c_str()));
            }
        }
        return st.top();
    }
};
