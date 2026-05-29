// LC 3. Longest Substring Without Repeating Characters
#include <string>
#include <unordered_map>

class Solution {
public:
    // LC 3 (last-index-jump form). The `it->second >= l` guard rejects
    // stale entries from outside the current window.
    int lengthOfLongestSubstring(std::string s) {
        std::unordered_map<char, int> last;
        int l = 0;
        int best = 0;
        for (int r = 0; r < static_cast<int>(s.size()); ++r) {
            char ch = s[r];
            auto it = last.find(ch);
            if (it != last.end() && it->second >= l) {
                l = it->second + 1;
            }
            last[ch] = r;
            if (r - l + 1 > best) {
                best = r - l + 1;
            }
        }
        return best;
    }
};
