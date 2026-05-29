# LC 125. Valid Palindrome
# Two pointers converging from the ends, skipping non-alphanumerics, with
# case-folded comparison. The empty string and single-char strings count
# as palindromes. O(n), O(1).
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
