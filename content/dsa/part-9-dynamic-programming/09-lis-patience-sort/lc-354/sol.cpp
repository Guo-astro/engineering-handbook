// LC 354. Russian Doll Envelopes
#include <vector>
#include <algorithm>

class Sol {
public:
    static int lengthOfLis(const std::vector<int>& nums) {
        std::vector<int> tails;
        for (int x : nums) {
            auto it = std::lower_bound(tails.begin(), tails.end(), x);
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
        }
        return static_cast<int>(tails.size());
    }

    static int maxEnvelopes(std::vector<std::vector<int>> envelopes) {
        if (envelopes.empty()) return 0;
        std::sort(envelopes.begin(), envelopes.end(),
                  [](const std::vector<int>& a, const std::vector<int>& b) {
                      if (a[0] != b[0]) return a[0] < b[0];
                      return a[1] > b[1];           // height DESC on width tie
                  });
        std::vector<int> heights;
        heights.reserve(envelopes.size());
        for (const auto& e : envelopes) heights.push_back(e[1]);
        return lengthOfLis(heights);
    }
};
