// LC 227. Basic Calculator II
#include <cctype>
#include <stack>
#include <string>

class Solution {
public:
    int calculate(const std::string& s) {
        std::stack<int> st;
        int num = 0;
        char op = '+';
        const std::size_t n = s.size();
        for (std::size_t i = 0; i < n; ++i) {
            char ch = s[i];
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                num = num * 10 + (ch - '0');
            }
            bool isLast = (i == n - 1);
            if ((!std::isdigit(static_cast<unsigned char>(ch)) && ch != ' ') || isLast) {
                if      (op == '+') st.push(num);
                else if (op == '-') st.push(-num);
                else if (op == '*') { int top = st.top(); st.pop(); st.push(top * num); }
                else                { int top = st.top(); st.pop(); st.push(top / num); }
                num = 0;
                op = ch;
            }
        }
        int total = 0;
        while (!st.empty()) { total += st.top(); st.pop(); }
        return total;
    }
};
