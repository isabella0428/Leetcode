class Solution1:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        # Time Limit Exceeded!
        def DFS(Sum, index, S, nums):
            nonlocal ans
            if index == len(nums):
                if Sum == S:
                    ans += 1
                return
            DFS(Sum + nums[index], index + 1, S, nums)
            DFS(Sum - nums[index], index + 1, S, nums)

        ans = 0
        DFS(0, 0, S, nums)
        return ans


class Solution2:
    # Memory Limit Exceeded!
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        # 0-1 Backpack
        # P: positive N:negative
        # sum(P) - sum(N) = target
        # sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
        # 2 * sum(P) = target + sum(nums)
        if (S + sum(nums)) % 2 or S > sum(nums):
            return 0
        target_P, n = int((S + sum(nums)) / 2), len(nums)
        dp = [0 for i in range(1 + target_P)]
        dp[0] = 1
        for num in nums:
            for i in range(target_P, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[target_P]


class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        n = len(nums)
        dp = [[0 for i in range(2001)] for j in range(n)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, n):
            for sum in range(-1000, 1001):
                if dp[i - 1][sum + 1000] > 0:
                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000]
                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000]
        return dp[n - 1][S + 1000] if S <= 1000 else 0


if __name__ == "__main__":
    a = Solution2()
    print(a.findTargetSumWays([0,0,0,0,0,0,0,0,1]
,1))
