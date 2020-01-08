import java.util.*;

class Solution1309 {
    public String freqAlphabets(String s) {
        String convertedS = "";
        for(int i = 0; i < s.length(); ++i) {
            if(i < s.length() - 2 && s.charAt(i + 2) == '#') {
                int subString = Integer.parseInt(s.substring(i, i + 2));
                convertedS += String.valueOf((char)((subString - 10) + 'j'));
                i += 2;
            }
            else {
                convertedS += String.valueOf((char)(s.charAt(i) - '1' + 'a'));
            }
        }
        return convertedS;
    }
}
