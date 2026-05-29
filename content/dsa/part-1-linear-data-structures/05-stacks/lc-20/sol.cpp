// LC 20. Valid Parentheses
// Push openers; on a closer, peek the top opener and pop iff it matches.
// Keying the pair table by closer keeps the lookup branch-free. The
// terminal stack-empty check rejects unmatched openers. O(n), O(n).
#include <stack>
#include <string>
#include <unordered_map>

bool isValid(const std::string& s) {
    std::unordered_map<char, char> pair = {
        {')', '('}, {']', '['}, {'}', '{'}
    };
    std::stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else {
            if (st.empty() || st.top() != pair[c]) return false;
            st.pop();
        }
    }
    return st.empty();
}
