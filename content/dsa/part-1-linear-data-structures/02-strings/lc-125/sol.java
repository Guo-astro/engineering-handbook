// LC 125. Valid Palindrome
// Two pointers converging from the ends, skipping non-alphanumerics, with
// case-folded comparison. The empty string and single-char strings count
// as palindromes. O(n), O(1).
public final class Sol {

    public boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) l++;
            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) r--;
            if (Character.toLowerCase(s.charAt(l))
                    != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    private Sol() {}
}
