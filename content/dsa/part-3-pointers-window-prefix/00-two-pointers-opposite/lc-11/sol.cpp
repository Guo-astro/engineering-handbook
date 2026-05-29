// LC 11. Container With Most Water
#include <vector>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int left = 0;
        int right = static_cast<int>(height.size()) - 1;
        int best = 0;
        while (left < right) {
            int hL = height[left];
            int hR = height[right];
            int width = right - left;
            if (hL < hR) {
                if (hL * width > best) best = hL * width;
                ++left;
            } else {
                if (hR * width > best) best = hR * width;
                --right;
            }
        }
        return best;
    }
};
