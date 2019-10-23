class MySolution:
    def wiggleMaxLength(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        n = len(diff)
        # dp[i] : maximum length of sequence that ended with diff[i]
        dp = [int(diff[i] != 0) for i in range(n)]
        for i in range(n):
            if diff[i] == 0:
                continue
            for j in range(i):
                if diff[i] * diff[j] < 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1


class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) < 2:
            return len(nums)
        up = 2 if nums[1] - nums[0] > 0 else 1
        down = 2 if nums[1] - nums[0] < 0 else 1
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                up = down + 1
            elif nums[i] - nums[i - 1] < 0:
                down = up + 1
        return max(up, down)

if __name__ == "__main__":
    a = Solution()
    print(a.wiggleMaxLength([1,7,4,9,2,5]))