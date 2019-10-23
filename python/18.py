class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = {}
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    new = a + b + nums[l] + nums[r]
                    if new == target:
                        tmp = [a, b, nums[l], nums[r]]
                        tmp.sort()
                        ans[tuple(tmp)] = 1
                    if new > target:
                        r -= 1
                    else:
                        l += 1
        result = []
        for item in ans.keys():
            result.append(list(item))
        return sorted(result)


if __name__ == "__main__":
    a = Solution()
    print(a.fourSum([1, 0, -1, 0, -2, 2], 0))


