class Solution1209 {
    public String removeDuplicates(String s, int k) {
        char[] stack = s.toCharArray();
        int[] count = new int[stack.length];
        int i =  0;
        for(int j = 0; j < stack.length; ++i, ++j) {
            stack[i] = stack[j];
            count[i] = i > 0 && stack[i - 1] == stack[i] ? count[i - 1] + 1 : 1;
            if(count[i] >= k)
                i -= k;
        }
        return new String(stack, 0, i);
    }
}