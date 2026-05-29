// LC 739. Daily Temperatures
#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        int n = static_cast<int>(temperatures.size());
        std::vector<int> answer(n, 0);
        std::stack<int> st;
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && temperatures[st.top()] < temperatures[i]) {
                int j = st.top();
                st.pop();
                answer[j] = i - j;
            }
            st.push(i);
        }
        return answer;
    }
};
