import java.util.HashMap;

class Solution974 {
    public int subarraysDivByK(int[] A, int K) {
        HashMap<Integer, Integer> reminder_map = new HashMap<>();

        int prefix_sum = 0;
        reminder_map.put(0, 1);
        int total_count = 0;
    
        for (int a : A) {
            prefix_sum += a;
            int reminder = (prefix_sum % K + K) % K;
            int count = reminder_map.getOrDefault(reminder, 0);
            total_count += count;
            reminder_map.put(reminder, count + 1);
        }
        return total_count;
    }
}