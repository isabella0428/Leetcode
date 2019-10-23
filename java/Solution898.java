import java.util.*;

class Solution898 {
    public int subarrayBitwiseORs(int[] A) {
        Set<Integer> ans = new HashSet<>();
        Set<Integer> cur = new HashSet<>();
        cur.add(0);
        for(int a : A) {
            Set<Integer> cur2 = new HashSet<>();
            for(int y : cur) {
                cur2.add(y | a);
            }
            cur2.add(a);
            cur = cur2;
            ans.addAll(cur);
        }
        return ans.size();
    }
}