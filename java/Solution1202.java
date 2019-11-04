class Solution1202 {
    /*  Union Find */

    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int[] p = new int[s.length()];

        // Initlization of parents
        for (int i = 0; i < s.length(); ++i)
            p[i] = i;

        // Create subsets using edges
        for (int i = 0; i < pairs.size(); ++i) {
            List<Integer> pair = pairs.get(i);
            union(p, pair.get(0), pair.get(1));
        }

        // Key Function to order subsets
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int j = 0; j < s.length(); ++j) {
            int parent = find(p, j);
            if (!map.containsKey(parent)) {
                map.put(parent, new ArrayList<>());
            }
            map.get(parent).add(j);
        }

        char[] arr = s.toCharArray();
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            List<Integer> nums = entry.getValue();
            List<Character> temp = new ArrayList<>();
            for (int i : nums) {
                temp.add(arr[i]);
            }
            Collections.sort(temp);
            for (int k = 0; k < nums.size(); ++k)
                arr[nums.get(k)] = temp.get(k);
        }
        return new String(arr);
    }

    public void union(int[] p, int i, int j) {
        int i_p = find(p, i), j_p = find(p, j);
        if (i_p != j_p)
            p[i_p] = j_p;
    }

    public int find(int[] p, int j) {
        if (p[j] == j)
            return p[j];
        p[j] = find(p, p[j]);
        return p[j];
    }
}