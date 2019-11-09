import java.util.*;

class Solution1191 {
    public int kConcatenationMaxSum(int[] arr, int k) {
        long sum = 0;
        for (int i = 0; i < arr.length; ++i) {
            sum += arr[i];
        }

        long prev = prev(arr);
        long back = back(arr);

        if (k == 1)
            return (int) (Math.max(Math.max(prev, back), singleArray(arr)));

        if (k == 0)
            return 0;

        if (sum > 0)
            return (int) ((prev + sum * (k - 2) + back) % 1000000007);
        else {
            return (int) (Math.max(Math.max(Math.max((prev + back) % 1000000007, prev), back), singleArray(arr)));
        }
    }

    public long prev(int[] arr) {
        long max_sum = 0;
        long sum = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            sum = (sum + arr[i]) % 1000000007;
            if (sum > max_sum)
                max_sum = sum;
        }
        System.out.println(max_sum);
        return max_sum;
    }

    public long back(int[] arr) {
        long max_sum = 0;
        long sum = 0;
        for (int i = 0; i < arr.length; ++i) {
            sum = (sum + arr[i]) % 1000000007;
            if (sum > max_sum)
                max_sum = sum;
        }
        return max_sum;
    }

    public long singleArray(int[] arr) {
        long currentSum = 0;
        long maxSum = 0;
        for (int i = 0; i < arr.length; i++) {
            currentSum = currentSum > 0 ? (currentSum + arr[i]) % 1000000007 : arr[i];
            maxSum = Math.max(currentSum, maxSum);
        }
        return (maxSum % 1000000007);
    }
}