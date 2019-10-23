class Solution1:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        def reverse(nums, start, end):
            if start >= end:
                return
            ans = nums.copy()
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        i = len(nums) - 1
        while i > 0:
            if nums[i] <= nums[i - 1]:
                i -= 1
                continue
            break
        start = i - 1
        if start < 0:
            return reverse(nums, 0, len(nums) - 1)
        end = len(nums) - 1
        while nums[end] <= nums[start] and end >= 0:
            end -= 1
        nums[start], nums[end] = nums[end], nums[start]
        return reverse(nums, start + 1, len(nums) - 1)


class Solution2:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        start = len(nums) - 1
        while start > 0 and nums[start] <= nums[start - 1]:
            start -= 1
        loc = start - 1
        if loc < 0:
            nums[0:len(nums)] = nums[::-1]
            return
        change = len(nums) - 1
        while nums[change] <= nums[loc]:
            change -= 1
        nums[loc], nums[change] = nums[change], nums[loc]
        nums[loc + 1:len(nums)] = nums[loc + 1:len(nums)][::-1]


if __name__ == "__main__":
    a = Solution2()
    nums = [3, 2, 1]
    a.nextPermutation(nums)
    print(nums)