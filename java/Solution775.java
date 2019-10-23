class Solution775 {
    public boolean isIdealPermutation(int[] A) {
        return localInversion(A, 0) == globalInversion(A, 0);
    }
    
    public int localInversion(int[] A, int loc) {
        if(loc == A.length - 1)
            return 0;
        return A[loc] > A[loc + 1] ? 1 + localInversion(A, loc + 1) : localInversion(A, loc + 1);
    }
    
    public int globalInversion(int[] A, int loc) {
        if (loc == A.length - 1)
            return 0;
        
        int num = 0;    // The number of inversion caused by A[loc]
        for (int i = loc + 1; i < A.length; ++i) {
            if(A[loc] > A[i])
                num += 1;
        }
        return num + globalInversion(A, loc + 1);
    }
}