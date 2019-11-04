class Solution1247 {
    public int minimumSwap(String s1, String s2) {
        int xy_1 = 0, yx_1 = 0, c2_x = 0;
        for (int i = 0; i < s1.length(); ++i) {
            if (s1.charAt(i) == s2.charAt(i))
                continue;
            if (s1.charAt(i) == 'x')
                xy_1 += 1;
            else
                yx_1 += 1;
        }

        for (int i = 0; i < s2.length(); ++i) {
            if (s2.charAt(i) == s1.charAt(i))
                continue;
            if (s2.charAt(i) == 'x')
                c2_x += 1;
        }

        if (s1.length() != s2.length() || (xy_1 + c2_x) % 2 != 0)
            return -1;
        return (int) (xy_1 / 2) + (int) (yx_1 / 2) + 2 * (xy_1 % 2);
    }
}