import java.util.*;

class Solution1190 {
    public static String reverseParentheses(String s) {
        String newString = "";
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < s.length(); ++i) {
            newString += String.valueOf(s.charAt(i));
            if (s.charAt(i) == '(') {
                st.push(i);
            }
            if (s.charAt(i) == ')') {
                int prev = st.pop();
                StringBuilder sb = new StringBuilder();
                sb.append(newString.substring(prev, i + 1));
                newString = newString.substring(0, prev) + sb.reverse().toString();
                continue;
            }
        }
        String returnString = "";
        for(char c : newString.toCharArray()) {
            if (c != ')' && c != '(')
                returnString += String.valueOf(c);
        }

        return returnString; 
    }

    public static void main(String ... args) {
        System.out.println(reverseParentheses("a(bcdefghijkl(mno)p)q"));
    }
}