import java.util.*;

class Solution1218 {
    public static int longestSubsequence(int[] arr, int difference) {
        HashMap<Integer, Integer> dp = new HashMap<>();
        int longest_length = 1;
        for(int j = 0; j < arr.length; j++) {
            dp.put(arr[j], dp.getOrDefault(arr[j] - difference, 0) + 1);
            longest_length = Math.max(dp.get(arr[j]), longest_length);
        }
        return longest_length;
    }

    public static void main(String ... args) {
        int []input = {3,0,-3,4,-4,7,6};
        System.out.println(longestSubsequence(input, 3));
    }
}