import java.util.*;

class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        if (s.equals(""))
            return 0;

        int begin = 0, end = 0;
        HashSet<Character> set = new HashSet<>();
        int maxL = 1;

        while (begin < s.length() - 1) {
            while (end < s.length()) {
                char c = s.charAt(end);
                if (set.contains(c)) {
                    break;
                }
                set.add(c);
                end++;
            }

            maxL = maxL > end - begin ? maxL : end - begin;
            set.remove(s.charAt(begin));
            begin++;
        }
        return maxL;
    }
}