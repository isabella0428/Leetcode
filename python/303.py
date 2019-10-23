class NumArray:

    def __init__(self, nums: 'List[int]'):
        n = len(nums)
        self.sum = [0 for i in range(1 + n)]
        self.sum[1] = nums[0]
        for i in range(2, len(nums) + 1):
            self.sum[i] = self.sum[i - 1] + nums[i - 1]

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        return self.sum[j + 1] - self.sum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)