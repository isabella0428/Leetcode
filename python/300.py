class Solution:
    # dp[i] = max(dp[j]) + 1, ∀ 0 ≤ j < i
    # LIS = max(dp[i]), ∀ 0 ≤ i < n
    # O(n^2)
    # BinarySearch O(nlog(n))
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        n = len(nums)
        memo = [1 for i in range(n + 1)]    # longest increasing subsequence ended with ith element
        for i in range(1, n + 1):
            for j in range(i - 1):
                if nums[i - 1] > nums[j]:
                    memo[i] = max(memo[i], memo[j + 1] + 1)
        return max(memo)


if __name__ == "__main__":
    a = Solution()
    print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))