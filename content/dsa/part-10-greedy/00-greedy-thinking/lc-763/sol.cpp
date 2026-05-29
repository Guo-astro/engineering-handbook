// LC 763. Partition Labels
#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> partitionLabels(const std::string& s) {
        // last[c]: rightmost index at which character c appears.
        int last[26] = {0};
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            last[s[i] - 'a'] = i;
        }
        std::vector<int> parts;
        int start = 0;
        int end = 0;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            // Greedy step: extend the right boundary to the farthest
            // last-occurrence among characters in the current window.
            end = std::max(end, last[s[i] - 'a']);
            if (i == end) {
                parts.push_back(end - start + 1);
                start = i + 1;
            }
        }
        return parts;
    }
};
