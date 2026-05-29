// LC 84. Largest Rectangle in Histogram
#include <vector>
#include <stack>

class Solution {
public:
    int largestRectangleArea(std::vector<int>& heights) {
        int ans = 0;
        std::stack<int> st;
        int n = static_cast<int>(heights.size());
        for (int i = 0; i <= n; ++i) {
            int cur = (i == n) ? 0 : heights[i];
            while (!st.empty() && heights[st.top()] > cur) {
                int h = heights[st.top()];
                st.pop();
                int w = st.empty() ? i : i - st.top() - 1;
                if (h * w > ans) {
                    ans = h * w;
                }
            }
            st.push(i);
        }
        return ans;
    }
};
