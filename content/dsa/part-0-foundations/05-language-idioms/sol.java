import java.util.HashMap;
import java.util.Map;

public class Sol {
    public static Map<Character, Integer> countFreqs(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        return freq;
    }
}
