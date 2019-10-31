class Solution1208 {
    public int equalSubstring(String s, String t, int maxCost) {
        int current_cost = 0;
        int current_length = 0;
        int max_length = 0;
        int l = 0;
        int r = 0;

        for (l = 0; l < s.length() - 1; ++l) {
            while ((current_cost <= maxCost) && (r < t.length())) {
                int next_cost = Math.abs(t.charAt(r) - s.charAt(r));
                if (current_cost + next_cost <= maxCost) {
                    current_length += 1;
                    max_length = Math.max(current_length, max_length);
                    r += 1;
                    current_cost += next_cost;
                } else {
                    break;
                }
            }
            current_cost -= Math.abs(t.charAt(l) - s.charAt(l));
            current_length -= 1;
        }
        return max_length;
    }
}