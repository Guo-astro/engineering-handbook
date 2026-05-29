// LC 11. Container With Most Water
#include <vector>

int maxArea(const std::vector<int>& height) {
    int left = 0;
    int right = static_cast<int>(height.size()) - 1;
    int best = 0;
    while (left < right) {
        int hL = height[left];
        int hR = height[right];
        int width = right - left;
        if (hL < hR) {
            int area = hL * width;
            if (area > best) best = area;
            ++left;
        } else {
            int area = hR * width;
            if (area > best) best = area;
            --right;
        }
    }
    return best;
}
