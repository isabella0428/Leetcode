import java.util.*;

class Solution1189 {
    public int maxNumberOfBalloons(String text) {
        int b = 0, a = 0, l = 0, o = 0, n = 0;
        for (char c : text.toCharArray()) {
            if (c == 'b')
                b += 1;
            if (c == 'a')
                a += 1;
            if (c == 'l')
                l += 1;
            if (c == 'o')
                o += 1;
            if (c == 'n')
                n += 1;
        }

        int count = Integer.MAX_VALUE;
        count = Math.min(count, b);
        count = Math.min(count, a);
        count = Math.min(count, l / 2);
        count = Math.min(count, o / 2);
        count = Math.min(count, n);
        return count;
    }
}