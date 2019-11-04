class Solution1201 {
    public int nthUglyNumber(int n, int a, int b, int c) {
        int low = 0, high = 2 * 1000000000;
        int result = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            long num = (mid / a + mid / b + mid / c - mid / lcm(a, b) - mid / lcm(a, c) - mid / lcm(b, c)
                    + mid / lcm(lcm(a, b), c));
            if (num >= n) {
                high = mid - 1;
                result = mid;
            } else
                low = mid + 1;
        }
        return result;
    }

    public long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }

    public long gcd(long a, long b) {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }
}