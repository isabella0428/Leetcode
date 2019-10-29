import java.util.*;

class Solution1239 {
    /*
    Problem: 1239. Maximum Length of a Concatenated String with Unique Characters
    Given an array of strings arr. 
    String s is a concatenation of a sub-sequence of arr 
    which have unique characters.
    Return the maximum possible length of s.

    Solution:
    Just a simple DFS
    */

    static int max_length = 0;

    public static int maxLength(List<String> arr) {
        int[] count = new int[26];

        int i, j;
        for (i = 0; i < arr.size(); ++i) {
            for (int p = 0; p < 26; ++p) {
                count[p] = 0;
            }

            for (j = 0; j < arr.get(i).length(); ++j) {
                if (count[arr.get(i).charAt(j) - 'a'] != 0)
                    break;
                count[arr.get(i).charAt(j) - 'a'] += 1;
            }
            if (j == arr.get(i).length())
                DFS(i + 1, arr, count, arr.get(i).length(), arr.get(i));
        }
        return max_length;
    }

    public static void DFS(int i, List<String> arr, int[] count, int current_length, String prev) {
        if (max_length < current_length)
            max_length = current_length;

        if (i >= arr.size())
            return;

        int[] new_count = new int[26];
        int l, k;
        for (l = i; l < arr.size(); ++l) {
            for (int q = 0; q < 26; ++q) {
                new_count[q] = count[q];
            }

            for (k = 0; k < arr.get(l).length(); ++k) {
                if (new_count[arr.get(l).charAt(k) - 'a'] != 0)
                    break;
                new_count[arr.get(l).charAt(k) - 'a'] += 1;
            }
            if (k == arr.get(l).length()) {
                DFS(l + 1, arr, new_count, current_length + arr.get(l).length(), prev + arr.get(l));
            }
        }
    }

    public static void main(String ... args) {
        List<String> input = new ArrayList<>();
        input.add("cha");
        input.add("r");
        input.add("act");
        input.add("ers");
        System.out.println(maxLength(input));
    }
}