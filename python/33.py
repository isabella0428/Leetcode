class Solution1:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, start, end, target):
            if start > end:
                return -1
            medium = int((start + end) / 2)
            if nums[medium] == target:
                return medium
            else:
                if nums[medium] > target:
                    end = medium - 1
                else:
                    start = medium + 1
                return binarySearch(nums, start, end, target)
        if not nums:
            return -1
        val = min(nums)
        index = nums.index(val)
        if target == val:
            return index
        if target == nums[- 1]:
            return len(nums) - 1
        if target > nums[-1]:
            return binarySearch(nums, 0, index, target)
        else:
            return binarySearch(nums, index + 1, len(nums) - 1, target)


class Solution2:
    def search(self, nums, target) -> int:
        def findPivot(nums, l, r):
            mid = (l + r) >> 1
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return mid
            if mid != len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return mid + 1
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
            return findPivot(nums, l, r)

        def binarySearch(l, r, nums, target):
            if l > r:
                return -1
            mid = l + r >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            return binarySearch(l, r, nums, target)

        if nums[len(nums) - 1] >= nums[0]:
            pivot = 0
        else:
            pivot = findPivot(nums, 0, len(nums) - 1)
        if nums[pivot] <= target <= nums[len(nums) - 1]:
            return binarySearch(pivot, len(nums) - 1, nums, target)
        else:
            return binarySearch(0, pivot - 1, nums, target)


if __name__ == "__main__":
    a = Solution2()
    print(a.search([3,1], 0))