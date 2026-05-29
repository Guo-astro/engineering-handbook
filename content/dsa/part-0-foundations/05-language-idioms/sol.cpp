#include <string>
#include <unordered_map>

std::unordered_map<char, int> count_freqs(const std::string& s) {
    std::unordered_map<char, int> freq;
    for (char c : s) {
        ++freq[c];  // default-constructs to 0, then increments
    }
    return freq;
}
