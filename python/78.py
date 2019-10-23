class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def combinations(nums, tmp):
            nonlocal ans
            if tmp[-1] == nums[-1]:
                return
            for index in range(nums.index(tmp[-1]) + 1, len(nums)):
                tmp.append(nums[index])
                ans.append(tmp)
                combinations(nums, tmp[:])
                tmp = tmp[:-1]

        ans = [[]]
        for i in range(len(nums)):
            tmp = [nums[i]]
            ans.append(tmp)
            combinations(nums, tmp[:])
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.subsets(nums = [1,2,3]))
