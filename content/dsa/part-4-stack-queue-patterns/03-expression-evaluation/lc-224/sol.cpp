// LC 224. Basic Calculator
#include <cctype>
#include <stack>
#include <string>

class Solution {
public:
    int calculate(const std::string& s) {
        std::stack<int> st;
        int result = 0, num = 0, sign = 1;
        for (std::size_t i = 0; i < s.size(); ++i) {
            char ch = s[i];
            if (std::isdigit(static_cast<unsigned char>(ch))) {
                num = num * 10 + (ch - '0');
            } else if (ch == '+') {
                result += sign * num; num = 0; sign = 1;
            } else if (ch == '-') {
                result += sign * num; num = 0; sign = -1;
            } else if (ch == '(') {
                st.push(result); st.push(sign);
                result = 0; sign = 1;
            } else if (ch == ')') {
                result += sign * num; num = 0;
                result *= st.top(); st.pop();   // saved sign
                result += st.top(); st.pop();   // saved running result
            }
        }
        result += sign * num;
        return result;
    }
};
