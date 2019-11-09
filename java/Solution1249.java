import java.util.*;

class Solution1249 {
    public static String minRemoveToMakeValid(String s) {
        int open = 0;
        StringBuilder sb = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c == '(')
                open++;
            if (c == ')') {
                if (open <= 0) // Truncate the tail paratheses
                    continue;
                open--;
            }
            sb.append(c);
        }
        StringBuilder result = new StringBuilder();
        for (int n = sb.length() - 1; n >= 0; n--) {
            if (sb.charAt(n) == '(' && open-- > 0)
                continue; // Truncate front parentheses
            result.append(sb.charAt(n));
        }
        return result.reverse().toString();
    }

    public static void main(String... args) {
        System.out.println(minRemoveToMakeValid("lee(t(c)o)de)"));
    }
}