import java.util.*;

class Solution1207 {
    public boolean uniqueOccurrences(int[] arr) {
        int[] count = new int[2001];
        Set<Integer> occur = new HashSet<>();
        Set<Integer> num = new HashSet<>();
        for (int i = 0; i < arr.length; ++i) {
            if (!num.contains(arr[i]))
                num.add(arr[i]);
            count[arr[i] + 1000] += 1;
            System.out.println(String.format("%d %d", arr[i], count[arr[i] + 1000]));
        }
        for (int i = 0; i <= 2000; ++i) {
            if (count[i] != 0)
                occur.add(count[i]);
        }
        return occur.size() == num.size();
    }
}