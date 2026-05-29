// LC 125. Valid Palindrome
// Two pointers converging from the ends, skipping non-alphanumerics, with
// case-folded comparison. The empty string and single-char strings count
// as palindromes. O(n), O(1).
//
// std::isalnum / std::tolower take int but are only defined for values
// representable as unsigned char or EOF. A signed char with the high bit
// set is undefined behavior; the unsigned-char cast is mandatory.
#include <string>
#include <cctype>

class Solution {
public:
    bool isPalindrome(const std::string& s) {
        int l = 0, r = static_cast<int>(s.size()) - 1;
        while (l < r) {
            while (l < r && !std::isalnum(static_cast<unsigned char>(s[l]))) ++l;
            while (l < r && !std::isalnum(static_cast<unsigned char>(s[r]))) --r;
            char a = static_cast<char>(std::tolower(static_cast<unsigned char>(s[l])));
            char b = static_cast<char>(std::tolower(static_cast<unsigned char>(s[r])));
            if (a != b) return false;
            ++l;
            --r;
        }
        return true;
    }
};
