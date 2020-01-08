class Solution455 {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);

        int content = 0;
        int j = 0;
        for (int i = 0; i < g.length; ++i) {
            while (j < s.length && s[j] < g[i]) {
                ++j;
            }
            if (j >= s.length)
                return content;
            content += 1;
            j++;
        }
        return content;
    }
}