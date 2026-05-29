// LC 49. Group Anagrams
// Bucket by canonical form. The 26-int character-count signature is O(k)
// per string vs O(k log k) for sorted-string keys. The '#' delimiter
// prevents counts like {1, 11} from colliding with {11, 1}.
// O(N * k) time, O(N * k) space, for N strings of average length k.
#include <unordered_map>
#include <vector>
#include <string>
#include <array>

std::vector<std::vector<std::string>> groupAnagrams(const std::vector<std::string>& strs) {
    std::unordered_map<std::string, std::vector<std::string>> groups;
    for (const std::string& s : strs) {
        std::array<int, 26> counts{};
        for (char ch : s) {
            counts[ch - 'a']++;
        }
        std::string key;
        key.reserve(64);
        for (int c : counts) {
            key.push_back('#');
            key.append(std::to_string(c));
        }
        groups[key].push_back(s);
    }
    std::vector<std::vector<std::string>> out;
    out.reserve(groups.size());
    for (auto& kv : groups) {
        out.push_back(std::move(kv.second));
    }
    return out;
}
