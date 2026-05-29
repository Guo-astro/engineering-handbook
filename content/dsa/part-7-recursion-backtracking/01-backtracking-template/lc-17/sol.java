// LC 17. Letter Combinations of a Phone Number
import java.util.*;

public final class Sol {
    private static final String[] KEYPAD = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.isEmpty()) return result;
        StringBuilder path = new StringBuilder();
        backtrack(digits, 0, path, result);
        return result;
    }

    private void backtrack(String digits, int i,
                           StringBuilder path, List<String> result) {
        if (i == digits.length()) {
            result.add(path.toString());
            return;
        }
        String letters = KEYPAD[digits.charAt(i) - '0'];
        for (int k = 0; k < letters.length(); k++) {
            path.append(letters.charAt(k));        // 1. CHOOSE
            backtrack(digits, i + 1, path, result); // 2. EXPLORE
            path.deleteCharAt(path.length() - 1);  // 3. UNCHOOSE
        }
    }
}
