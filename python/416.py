class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        # Whether to pick it or not is a 0-1 backpack problem
        target, n = sum(nums) / 2, len(nums)
        if int(target) != target:
            return False
        else:
            target = int(target)
        dp = [[False for j in range(target + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        dp[0][0] = False
        for i in range(1 + n):
            for j in range(1 + target):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]





if __name__ == "__main__":
    a = Solution()
    print(a.canPartition([1, 5, 11, 5]))