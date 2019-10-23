class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        # search 0 ~ n - 2 or 1 ~ n - 1
        def circleRob(low, high, nums):
            prev1, prev2 = 0, 0
            for item in nums[low:high + 1]:
                tmp = prev1
                prev1 = max(prev2 + item, prev1)
                prev2 = tmp
            return prev1
        n = len(nums)
        notlast = circleRob(0, n - 2, nums)
        notfirst = circleRob(1, n - 1, nums)
        return max(notfirst, notlast) if n != 1 else nums[0]


if __name__ == "__main__":
    a = Solution()
    print(a.rob([1]))

