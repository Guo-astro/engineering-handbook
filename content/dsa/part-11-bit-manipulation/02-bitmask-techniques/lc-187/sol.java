// LC 187. Repeated DNA Sequences
import java.util.*;

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        if (s.length() < 10) return new ArrayList<>();
        int[] code = new int[26];
        code['A' - 'A'] = 0;
        code['C' - 'A'] = 1;
        code['G' - 'A'] = 2;
        code['T' - 'A'] = 3;
        int mask = 0;
        final int MASK20 = (1 << 20) - 1;     // 20 low bits; fits int comfortably
        Map<Integer, Integer> seen = new HashMap<>();
        List<String> answer = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            mask = ((mask << 2) | code[s.charAt(i) - 'A']) & MASK20;
            if (i >= 9) {
                int count = seen.merge(mask, 1, Integer::sum);
                if (count == 2) {
                    answer.add(s.substring(i - 9, i + 1));
                }
            }
        }
        return answer;
    }
}
