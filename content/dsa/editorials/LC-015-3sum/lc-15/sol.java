// LC 15. 3Sum
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public final class Sol {

    /** LC 15. Return every unique triplet of values summing to zero. */
    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int target = -nums[i];
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                int s = nums[l] + nums[r];
                if (s < target) {
                    l++;
                } else if (s > target) {
                    r--;
                } else {
                    out.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (l < r && nums[r] == nums[r + 1]) r--;
                }
            }
        }
        return out;
    }

    private Sol() {}
}
