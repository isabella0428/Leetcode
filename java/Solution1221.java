class Solution1221 {
    /***
     * 1221. Split a String in Balanced Strings 
     * Balanced strings are those who have equal quantity of 'L' and 'R' characters.
     * Given a balanced string s split it in the maximum amount of balanced strings. 
     * Return the maximum amount of splitted balanced strings.
     * 
     * Solution:
     * Suppose we have a balanced string which consist of N Rs and N Ls.
     * We can split it into two parts if the first halves is a balanced string
     * So we get most balanced strings if we cut off the shortest balanced strings.
     */

    public int balancedStringSplit(String s) {
        int L_num = 0;
        int R_num = 0;
        int sum = 0;

        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == 'L')
                L_num += 1;
            else
                R_num += 1;
            if (L_num == R_num) {
                sum += 1;
                L_num = 0;
                R_num = 0;
            }
        }
        return sum;
    }
}