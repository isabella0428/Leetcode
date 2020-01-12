import java.util.*;

class Solution870 {
    public int[] advantageCount(int[] A, int[] B) {
        int[] new_A = A.clone();
        Arrays.sort(new_A);
        int[] new_B = B.clone();
        Arrays.sort(new_B);
        int[] res_A = new int[A.length];
        HashMap<Integer, Deque<Integer>> map = new HashMap<>();
        Deque<Integer> remaining = new LinkedList<>();

        for (int b : new_B) {
            map.put(b, new LinkedList<Integer>());
        }

        int j = 0;
        for (int a : new_A) {
            if(a > new_B[j]) {
                map.get(new_B[j++]).add(a);
            }
            else{
                remaining.add(a);
            }
        }

        for (int t = 0; t < A.length; ++t) {
            if (!map.get(B[t]).isEmpty()) {
                res_A[t] = map.get(B[t]).pop();
            } else {
                res_A[t] = remaining.pop();
            }
        }
        return res_A;
    }
}