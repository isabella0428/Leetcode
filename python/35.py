class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if target < nums[i]:
                return i
        return i + 1


class Solution2:
    def searchInsert(self, nums, target) -> int:
        def binarySearch(l, r, nums, target):
            mid = l + r >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
                if nums[r] < target:
                    return r + 1
            else:
                l = mid + 1
                if nums[l] > target:
                    return l
            return binarySearch(l, r, nums, target)

        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        return binarySearch(0, len(nums) - 1, nums, target)


if __name__ == "__main__":
    a = Solution2()
    print(a.searchInsert([1, 3, 5, 6], 7))