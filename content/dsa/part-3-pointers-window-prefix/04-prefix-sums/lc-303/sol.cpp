// LC 303. Range Sum Query - Immutable
#include <vector>

class NumArray {
public:
    explicit NumArray(const std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        // prefix has length n + 1; prefix[0] = 0 is the empty-sum sentinel.
        prefix_.assign(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix_[i + 1] = prefix_[i] + nums[i];
        }
    }

    int sumRange(int left, int right) const {
        return static_cast<int>(prefix_[right + 1] - prefix_[left]);
    }

private:
    std::vector<long long> prefix_;
};
