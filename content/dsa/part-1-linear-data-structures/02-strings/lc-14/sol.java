// LC 14. Longest Common Prefix
// Vertical scanning: walk columns of strs[0]; on first mismatch (or running
// off the end of any string), return the prefix up to that column.
// O(S) where S = sum of lengths, O(1) extra space.
public final class Sol {

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        String first = strs[0];
        for (int i = 0; i < first.length(); i++) {
            char c = first.charAt(i);
            for (int k = 1; k < strs.length; k++) {
                if (i >= strs[k].length() || strs[k].charAt(i) != c) {
                    return first.substring(0, i);
                }
            }
        }
        return first;
    }

    private Sol() {}
}
