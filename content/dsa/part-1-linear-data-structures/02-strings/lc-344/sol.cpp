// LC 344. Reverse String
// Two-pointer in-place swap. LC's C++ signature uses vector<char> to match
// the cross-language harness, even though std::string is also mutable.
// O(n), O(1).
#include <vector>
#include <utility>

class Solution {
public:
    void reverseString(std::vector<char>& s) {
        int l = 0, r = static_cast<int>(s.size()) - 1;
        while (l < r) {
            std::swap(s[l], s[r]);
            ++l;
            --r;
        }
    }
};
