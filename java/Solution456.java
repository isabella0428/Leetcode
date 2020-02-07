class Solution456 {
    public boolean find132pattern(int[] nums) {
        for (int j = nums.length - 1; j >= 0; --j) {
            int c = nums[j];
            int smaller = 0, bigger = 0;
            for (int i = 0; i < j; ++i) {
                if (nums[i] < c)
                    smaller = 1;
                if (smaller == 1 && nums[i] > c)
                    bigger = 1;
                if (smaller == 1 && bigger == 1) {
                    return true;
                }
            }
        }
        return false;
    }
}