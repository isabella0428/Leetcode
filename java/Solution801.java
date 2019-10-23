class Solution801 {
    public static int minSwap(int[] A, int[] B) {
        // s1: cost without swapping (i - 1)th bit  n1: cost with swapping ith bit
        int s1, n1, s2, n2; 
        int length = A.length;
        
        s1 = 0;
        n1 = 1;
        n2 = length;
        s2 = length;
        
        for(int i = 1; i < length; ++i) {
            s2 = length;
            n2 = length;
            if (A[i] > A[i - 1] && B[i] > B[i - 1])
            {
                s2 = Math.min(s1, s2);
                n2 = Math.min(n2, n1 + 1);
            }
            if (B[i] > A[i - 1]  && A[i] > B[i - 1])
            {
                n2 = Math.min(s1 + 1, n2);
                s2 = Math.min(n1, s2);
            }

            s1 = s2;
            n1 = n2;
        }
        return Math.min(n2, s2);
    }

    public static void main(String ... args) {
        int A[] = {1, 3, 5, 4};
        int B[] = {1, 2, 3, 7};
        System.out.println(minSwap(A, B));
    }
}