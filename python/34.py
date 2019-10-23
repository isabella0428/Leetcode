class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, start, end, ans, target):
            if start > end:
                return
            if nums[start] > target or nums[end] < target:
                return
            medium = int((start + end) / 2)
            if nums[medium] < target:
                start = medium + 1
                return binarySearch(nums, start, end, ans, target)
            elif nums[medium] > target:
                end = medium - 1
                return binarySearch(nums, start, end, ans, target)
            else:
                if medium < ans[0]:
                    ans[0] = medium
                if medium > ans[1]:
                    ans[1] = medium
                binarySearch(nums, start, medium - 1, ans,target)
                binarySearch(nums, medium + 1, end, ans, target)

        if not nums:
            return [-1, -1]
        ans = [float('inf'), -1]
        start, end = 0, len(nums) - 1
        medium = int((start + end) / 2)
        if nums[medium] < target:
            start = medium + 1
            binarySearch(nums, start, end, ans, target)
        elif nums[medium] > target:
            end = medium - 1
            binarySearch(nums, start, end, ans, target)
        else:
            if medium < ans[0]:
                ans[0] = medium
            if medium > ans[1]:
                ans[1] = medium
            binarySearch(nums, start, medium - 1, ans, target)
            binarySearch(nums, medium + 1, end, ans, target)
        if ans == [float('inf'), -1]:
            return [-1, -1]
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.searchRange([1], 1))