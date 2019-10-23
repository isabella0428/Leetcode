class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        n = len(nums)
        money = [0 for i in range(n + 1)]
        prev1 = 0
        prev2 = 0
        for item in nums:
            tmp = prev1
            prev1 = max(prev2 + item, prev1)
            prev2 = tmp

        return prev1


if __name__ == "__main__":
    a = Solution()
    print(a.rob([1,2,3,1]))