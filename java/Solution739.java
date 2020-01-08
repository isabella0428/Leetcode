class Solution739 {
    public int[] dailyTemperatures(int[] T) {
        int[] stack = new int[T.length];
        int[] ret = new int[T.length];
        int top = -1;

        for (int i = 0; i < T.length; ++i) {
            while (top >= 0 && T[i] > T[stack[top]]) {
                int idx = stack[top--];
                ret[idx] = i - idx;
            }
            stack[++top] = i;
        }
        return ret;
    }
}