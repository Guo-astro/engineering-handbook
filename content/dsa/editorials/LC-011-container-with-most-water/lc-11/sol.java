// LC 11. Container With Most Water

public final class Sol {

    /** LC 11. Maximum water area between two walls in height[]. O(n) / O(1). */
    public static int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int best = 0;
        while (left < right) {
            int hL = height[left];
            int hR = height[right];
            int width = right - left;
            if (hL < hR) {
                int area = hL * width;
                if (area > best) best = area;
                left++;
            } else {
                int area = hR * width;
                if (area > best) best = area;
                right--;
            }
        }
        return best;
    }

    private Sol() {}
}
