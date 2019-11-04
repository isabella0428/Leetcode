import java.util.*;

class Solution1248 {
    public static int numberOfSubarrays(int[] nums, int k) {
       return atMost(nums, k) - atMost(nums, k - 1); 
    }

    public static int atMost(int[] A, int k) {
        int i = 0, res = 0;
        for(int j = 0; j < A.length; ++j) {
            k -= A[j] % 2;
            while(k < 0)
                k += A[i++] % 2;
            res += j - i + 1;
        }
        return res;
    }

    public static void main(String ... args) {
        int[] num = {2,2,2,1,2,2,1,2,2,2};
        System.out.println(numberOfSubarrays(num, 2));
    }
}