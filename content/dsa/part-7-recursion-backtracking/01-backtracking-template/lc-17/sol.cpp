// LC 17. Letter Combinations of a Phone Number
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> letterCombinations(std::string digits) {
        std::vector<std::string> result;
        if (digits.empty()) return result;
        std::string path;
        backtrack(digits, 0, path, result);
        return result;
    }

private:
    static constexpr const char* KEYPAD[10] = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    void backtrack(const std::string& digits, int i,
                   std::string& path,
                   std::vector<std::string>& result) {
        if (i == static_cast<int>(digits.size())) {
            result.push_back(path);
            return;
        }
        const char* letters = KEYPAD[digits[i] - '0'];
        for (int k = 0; letters[k] != '\0'; k++) {
            path.push_back(letters[k]);              // 1. CHOOSE
            backtrack(digits, i + 1, path, result);  // 2. EXPLORE
            path.pop_back();                         // 3. UNCHOOSE
        }
    }
};
