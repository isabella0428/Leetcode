class Solution1310 {
    /*
    	a ^ a = 0, Use this property to reduce complexity  
    */
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] res = new int[queries.length];
        for(int i = 1; i < arr.length; ++i) {
            arr[i] ^= arr[i - 1];
        }
        for(int j = 0; j < queries.length; ++j) {
            int[] q = queries[j];
            if(q[0] == 0) {
                res[j] = arr[q[1]];
            }
            else {
                res[j] = arr[q[0] - 1] ^ arr[q[1]];
            }
        }
        return res;
    }
}
