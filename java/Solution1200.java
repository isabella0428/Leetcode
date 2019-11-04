class Solution1200 {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int mini = Integer.MAX_VALUE;
        Map<Integer, List<List<Integer>>> map = new HashMap<>();

        for (int i = 1; i < arr.length; ++i) {
            List<List<Integer>> value = map.getOrDefault(arr[i] - arr[i - 1], new ArrayList<List<Integer>>());
            value.add(Arrays.asList(arr[i - 1], arr[i]));
            map.put(arr[i] - arr[i - 1], value);
            mini = Math.min(mini, arr[i] - arr[i - 1]);
        }
        return map.get(mini);
    }
}