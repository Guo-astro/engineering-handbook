// LC 344. Reverse String
// Two-pointer in-place swap on a mutable character buffer.
// Java String is final, so the LC signature uses char[]. O(n), O(1).
public final class Sol {

    public void reverseString(char[] s) {
        int l = 0, r = s.length - 1;
        while (l < r) {
            char tmp = s[l];
            s[l] = s[r];
            s[r] = tmp;
            l++;
            r--;
        }
    }

    private Sol() {}
}
