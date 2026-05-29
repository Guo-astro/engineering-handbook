// LC 3. Longest Substring Without Repeating Characters
#include <string>
#include <vector>

int lengthOfLongestSubstring(const std::string& s) {
    // ASCII-128 last-index array. The cast to unsigned char is required:
    // on platforms where char is signed (most x86/ARM Linux/macOS), an
    // extended-ASCII byte would index negatively and read out of bounds.
    std::vector<int> lastIndex(128, -1);
    int l = 0;
    int best = 0;
    for (int r = 0; r < static_cast<int>(s.size()); ++r) {
        unsigned char c = static_cast<unsigned char>(s[r]);
        if (lastIndex[c] >= l) {
            l = lastIndex[c] + 1;
        }
        lastIndex[c] = r;
        if (r - l + 1 > best) {
            best = r - l + 1;
        }
    }
    return best;
}
