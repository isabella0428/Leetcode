import java.util.*;

class Solution1234 {
    public static void main(String ... args) {
        System.out.println(balancedString("QQQQ"));
    }

    public static int balancedString(String s) {
        int [] count = new int[128];
        int length = s.length();
        int k = length / 4;
        int i = 0;
        int ret = length;
        for (int j = 0; j < length; ++j) {
            ++count[s.charAt(j)];
        }

        for (int j = 0; j < length; ++j) {
            --count[s.charAt(j)];
            while(i < length && count['Q'] <= k && count['E'] <= k && count['W'] <= k && count['R'] <= k) {
                ret = Math.min(ret, j - i + 1);
                ++count[s.charAt(i++)];
            }
        }
        return ret;
    }
}