// LC 187. Repeated DNA Sequences
#include <string>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<std::string> findRepeatedDnaSequences(const std::string& s) {
        if (s.size() < 10) return {};
        int code[26] = {0};
        code['A' - 'A'] = 0;
        code['C' - 'A'] = 1;
        code['G' - 'A'] = 2;
        code['T' - 'A'] = 3;
        int mask = 0;
        const int MASK20 = (1 << 20) - 1;
        std::unordered_map<int, int> seen;
        std::vector<std::string> answer;
        for (int i = 0; i < static_cast<int>(s.size()); ++i) {
            mask = ((mask << 2) | code[s[i] - 'A']) & MASK20;
            if (i >= 9) {
                if (++seen[mask] == 2) {
                    answer.push_back(s.substr(i - 9, 10));
                }
            }
        }
        return answer;
    }
};
