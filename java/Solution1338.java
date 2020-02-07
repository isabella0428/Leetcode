import java.util.*;

class Solution1338 {
    public int minSetSize(int[] arr) {
        PriorityQueue<int[]> maxQ = new PriorityQueue<>((a, b) -> a[1] != b[1] ? b[1] - a[1] : b[0] - a[0]);
        int total_length = arr.length;
        Map<Integer, Integer> map = new HashMap<>();
        HashSet<Integer> all_numbers = new HashSet<>();
        
        for (int a : arr) {
            map.put(a, map.getOrDefault(a, 0) + 1);
            all_numbers.add(a);
        }
        
        for(int b : all_numbers) {
            maxQ.offer(new int[]{b, map.get(b)});
        }
        
        int num = 0;
        int cur_length = total_length;
        while(maxQ.size() > 0) {
            ++num;
            cur_length -= maxQ.poll()[1];
            if (cur_length <= total_length / 2) {
                break;
            }
        }
        return num;
    }
}