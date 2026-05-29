// LC 242. Valid Anagram
// Increment-decrement-and-check: build a counter from s, then walk t
// decrementing; any underflow means t is not a permutation of s.
// Length short-circuit avoids building the counter when sizes differ.
// O(n), O(k) where k is the alphabet size.
#include <unordered_map>
#include <string>

bool isAnagram(const std::string& s, const std::string& t) {
    if (s.size() != t.size()) {
        return false;
    }
    std::unordered_map<char, int> counts;
    for (char ch : s) {
        counts[ch]++;
    }
    for (char ch : t) {
        auto it = counts.find(ch);
        if (it == counts.end() || it->second == 0) {
            return false;
        }
        it->second--;
    }
    return true;
}
