class Solution:
    def combinationSum4(self, nums: 'List[int]', target: 'int') -> 'int':
        dp = [0 for i in range(1 + target)]
        dp[0] = 1
        for v in range(1, 1 + target):
            for num in nums:
                if v >= num:
                    dp[v] += dp[v - num]
        return dp[target]


if __name__ == "__main__":
    a = Solution()
    print(a.combinationSum4([1,2,3], 4))