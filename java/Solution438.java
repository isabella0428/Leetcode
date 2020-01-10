import java.util.*;

class Solution438 {
    public List<Integer> findAnagrams(String s, String p) {
        // s: source string p:target string
        // Find all anagrams of p in s

        // Extreme conditions
        if (p.length() > s.length()) {
            return new ArrayList<>();
        }

        List<Integer> res = new ArrayList<>();
        Map<Character, Integer> map = new HashMap<>();

        // Caculate each character's appearance numbers
        for (char c : p.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        // Two partition points of sliding window
        int begin = 0, end = 0;
        int count = map.size();
        while (end < s.length()) {
            // Move end to right
            char t = s.charAt(end);
            if (map.containsKey(t)) {
                map.put(t, map.get(t) - 1);
                if (map.get(t) == 0) {
                    count--;
                }
            }
            end++;

            while (count == 0) {
                // Check if begin is the right answer
                if (end - begin == p.length()) {
                    res.add(begin);
                    break;
                }

                // Move begin to right
                char k = s.charAt(begin);
                if (map.containsKey(k)) {
                    map.put(k, map.get(k) + 1);
                    if (map.get(k) > 0)
                        count++;
                }
                begin++;
            }
        }
        return res;
    }
}