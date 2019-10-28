/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     public int f(int x, int y);
 * };
 */
class Solution1237 {
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        List<List<Integer>> result = new ArrayList<>();
        int l = 1;
        int r = 1000;

        for (int x = 1; x < 1000; ++x) {
            List<Integer> list = BinarySearch(customfunction, z, l, r, x);
            if (list != null) {
                result.add(list);
                r = list.get(1);
            } else
                continue;
        }
        return result;
    }

    public List<Integer> BinarySearch(CustomFunction customfunction, int z, int l, int r, int x) {
        if (l > r) {
            return null;
        }
        int m = (l + r) / 2;
        if (customfunction.f(x, m) == z) {
            List<Integer> list = new ArrayList<>();
            list.add(x);
            list.add(m);
            return list;
        }

        if (customfunction.f(x, m) > z) {
            return BinarySearch(customfunction, z, l, m - 1, x);
        }
        return BinarySearch(customfunction, z, m + 1, r, x);
    }
}